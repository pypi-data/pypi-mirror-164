import os
import sys
import argparse
import traceback
import csv
import json
import yaml
from pathlib import Path
from io import StringIO

yaml.Dumper.ignore_aliases = lambda *args: True


# common

def parse_args(argv):
    self_name = os.path.basename(argv[0])
    parser = argparse.ArgumentParser(prog=self_name,
                                     description="{JSON,YAML,SV} to {JSON,JAML,SV,MD} converting tool (supports objects, object lists and plain entities)")
    parser.add_argument("-i", "--input-file", type=str, help="Input file (stdin if not specified)")
    parser.add_argument("-o", "--output-file", type=str, help="Output file (stdout if not specified)")
    parser.add_argument("-f", "--from-format", type=str, help="Input data format")
    parser.add_argument("-t", "--to-format", type=str, help="Output data format")
    parser.add_argument("--in-with-header", action="store_true", help="Input has a header")
    parser.add_argument("-d", "--delimiter", type=str, help="Delimiter")
    parser.add_argument("--in-type", help="Type (list, object, single) - for input SV")
    parser.add_argument("--in-header", help="Input header spec - for input SV")
    parser.add_argument("--out-no-header", action="store_true", help="Dont't print header - for output SV")
    parser.add_argument("--out-no-data", action="store_true", help="Don't print data - for output SV")
    parser.add_argument("--out-type-spec", help="Data types spec (supported: longlink, shortlink or nothing) - for output SV")
    return parser.parse_args(sys.argv[1:])


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def eprint_exception(e, print_traceback=True, need_exit=True):
    eprint(e)
    if print_traceback:
        eprint(traceback.format_exc())
    if need_exit:
        exit(1)


class ObjDataConverter:

    def __init__(self, args):
        self.args = args
        conf_file = "{}/.config/objdc.yaml".format(str(Path.home()))
        self.conf_file_object = {"main": {"print_traceback": True}}
        try:
            with open(conf_file, "r") as f:
                self.conf_file_object = yaml.safe_load(f)
        except Exception as e:
            pass

    def get_confs(self):
        return self.conf_file_object

    def get_args(self):
        return self.args

    def custom_open_input(self, filename=None):
        global inp_f
        confs = self.get_confs()
        args = self.get_args()
        print_traceback = confs["main"]["print_traceback"]
        input_file_name = args.input_file
        if filename is not None:
            input_file_name = filename
        if input_file_name is not None:
            try:
                inp_f = open(input_file_name, "r")
            except Exception as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            inp_f = sys.stdin
        return inp_f

    def custom_open_output(self, filename=None):
        global out_f
        confs = self.get_confs()
        args = self.get_args()
        print_traceback = confs["main"]["print_traceback"]
        output_file_name = args.output_file
        if filename is not None:
            output_file_name = filename
        if output_file_name is not None:
            try:
                out_f = open(output_file_name, "r")
            except Exception as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            out_f = sys.stdout
        return out_f

    def custom_close_input(self, inp_f):
        # confs = self.get_confs()
        args = self.get_args()
        # print_traceback=confs["main"]["print_traceback"]
        if args.input_file is not None:
            inp_f.close()

    def custom_close_output(self, out_f):
        # confs = self.get_confs()
        args = self.get_args()
        # print_traceback=confs["main"]["print_traceback"]
        if args.output_file is not None:
            out_f.close()

    # sepval

    def sepval_load(self, f, with_header=None, delimiter=None, header=None, type=None):
        ret = None
        if delimiter is None:
            delimiter = "|"
        if type is None or type == "list":
            ret = []
            if with_header:
                reader = csv.DictReader(f, delimiter=delimiter)
                for i in reader:
                    ret.append(i)
            else:
                if header is not None:
                    reader = csv.DictReader(f, delimiter=delimiter, fieldnames=header)
                    for i in reader:
                        ret.append(i)
                else:
                    reader = csv.reader(f, delimiter=delimiter)
                    for i in reader:
                        ret.append({j: i[j] for j in range(0, len(i))})
        elif type == "object":
            ret = {}
            reader = csv.DictReader(f, delimiter=delimiter, fieldnames=["key", "value"])
            for i in reader:
                ret[i["key"]] = i["value"]
        elif type == "single":
            ret = f.read()
        else:
            sys.stderr.write("Unknown type: {}\n".format(type))
            exit(1)
        return ret

    def sepval_dump(self, data, f, delimiter=None, no_header=None, no_data=None):
        if delimiter is None:
            delimiter = "|"
        if isinstance(data, list):
            writer = csv.DictWriter(sys.stdout, delimiter=delimiter, fieldnames=data[0].keys(), extrasaction='ignore')
            if not no_header:
                writer.writeheader()
            if not no_data:
                for row in data:
                    writer.writerow(row)
        elif isinstance(data, dict):
            if not no_header:
                f.write("key" + delimiter + "value\n")
            for k in data:
                f.write(k + delimiter + str(data[k]) + "\n")
        else:
            f.write(data)

    def sepval_loads(self, s, **kwargs):
        f = StringIO(s)
        self.sepval_load(f, kwargs)

    def sepval_dumps(self, data, **kwargs):
        f = StringIO()
        self.sepval_dump(data, f, kwargs)
        return f.getvalue()

    def get_type_spec(self, type_spec, position):
        if not isinstance(type_spec, list):
            return ""
        else:
            if position > len(type_spec) - 1:
                return ""
            else:
                return type_spec[position]

    # markdown

    def md_linkify(self, l, link_text):
        return ('[{}]({})'.format(link_text, l))

    def md_write_header(self, f, fieldnames):
        res = "|"
        line = "|"
        for i in fieldnames:
            res = "{}{}|".format(res, i)
            line = "{}{}|".format(line, "-")
        f.write(res + "\n" + line + "\n")

    def md_write_row(self, f, row_obj, fieldnames, type_spec):
        res = "|"
        count = 0
        for i in fieldnames:
            value = ""
            if i in row_obj.keys():
                value = row_obj[i]
            t = self.get_type_spec(type_spec, count)
            if t == "shortlink" or t == "longlink":
                link_text = "link"
                if t == "shortlink":
                    link_text = value
                value = self.md_linkify(value, link_text)
            res = "{}{}|".format(res, value)
            count = count + 1
        f.write(res + "\n")

    def md_dump(self, data, f, type_spec=None):
        if isinstance(data, list):
            if len(data) != 0:
                fieldnames = data[0].keys()
                self.md_write_header(f, fieldnames)
                for i in data:
                    self.md_write_row(f, i, fieldnames, type_spec)
        elif isinstance(data, dict):
            fieldnames = ["key", "value"]
            self.md_write_header(f, fieldnames)
            for i in data:
                self.md_write_row(f, {fieldnames[0]: i, fieldnames[1]: data[i]}, fieldnames, ["", ""])
        else:
            f.write(data)

    def md_dumps(self, data, **kwargs):
        f = StringIO()
        self.md_dump(data, f, kwargs)
        return f.getvalue()

    # load-dump

    def custom_load(self, inp_f):
        confs = self.get_confs()
        args = self.get_args()
        print_traceback = confs["main"]["print_traceback"]
        from_format = "json"
        if args.from_format is not None:
            from_format = args.from_format.lower()
        if from_format not in ["json", "yaml", "sv"]:
            eprint("Unsupported input format: {}".format(from_format))
            return None
        input_obj = None
        try:
            if from_format == "json":
                input_obj = json.load(inp_f)
            if from_format == "yaml":
                input_obj = yaml.safe_load(inp_f)
            if from_format == "sv":
                prepared_header = None
                if args.in_header is not None:
                    f = StringIO(args.in_header)
                    h_reader = csv.reader(f, delimiter=",")
                    prepared_header = next(h_reader)
                input_obj = self.sepval_load(inp_f, args.in_with_header, args.delimiter, prepared_header, args.in_type)
        except Exception as e:
            eprint_exception(e, print_traceback=print_traceback)
        return input_obj

    def custom_dump(self, out_f, output_obj):
        confs = self.get_confs()
        args = self.get_args()
        print_traceback = confs["main"]["print_traceback"]
        to_format = "json"
        if args.to_format != None:
            to_format = args.to_format.lower()
        if to_format not in ["json", "yaml", "sv", "md"]:
            eprint("Unsupported output format: {}".format(to_format))
            return None
        try:
            if to_format == "json":
                json.dump(output_obj, out_f, indent=4, ensure_ascii=False)
            if to_format == "yaml":
                yaml.dump(output_obj, out_f, default_flow_style=False, allow_unicode=True)
            if to_format == "sv":
                self.sepval_dump(output_obj, out_f, args.delimiter, args.out_no_header, args.out_no_data)
            if to_format == "md":
                prepared_type_spec = None
                if args.out_type_spec is not None:
                    f = StringIO(args.out_type_spec)
                    h_reader = csv.reader(f, delimiter=",")
                    prepared_type_spec = next(h_reader)
                self.md_dump(output_obj, out_f, prepared_type_spec)
        except Exception as e:
            eprint_exception(e, print_traceback=print_traceback)
