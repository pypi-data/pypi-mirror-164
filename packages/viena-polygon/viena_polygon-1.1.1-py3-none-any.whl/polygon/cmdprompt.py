import cmd, sys
from turtle import *
from polygon import parse
from polygon import rest_connect
import json
import typer
import simplejson
import traceback
class PolygonShell(cmd.Cmd):
    intro = 'Welcome to the Polygon Query shell.   Type help or ? to list commands.\n'
    prompt = '>'
    file = None

    # ----- basic turtle commands -----
    def do_select(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        sqlResult=""
        try:
            data = ("**** polygon: query **** \n"
                    " ##  Below are the tables can be queried\n"
                    "        image,dataset,annotation,training_set,version\n"
                    " ##  Sql query :\n"
                    " ##      Example: \n"
                    "               1. select * from images\n"
                    "               2. select * from dataset limit 5\n"
                    "               3. select objectName from annotation\n"
                    " ##  No sql query : \n"
                    "        Example: \n"
                    "                 db.<table_name>.find({'<column_name>':'<value>'})\n"
                    "                 db.<table_name>.count({'<column_name>':'<value>'})")

            if '|' in arg:
                x=arg.split("|")
                args=x[0]
                outptDisplay =True
            else:
                args=arg
                outptDisplay =False
            query="select "+ str(args)
            parsedData=parse.parse_sql(query)
            sqlResult = rest_connect.sqlreslt(parsedData)

            error1 = sqlResult["error"]
            cnt = sqlResult["count"]
            res = sqlResult["results"]
            if (error1 != None):
                print(sqlResult)
                print('\033[92m' +data)
            elif (outptDisplay == True):
                x={
                    "count":cnt,
                    "results":res,
                }
                data = simplejson.dumps(x, indent=4)
                cnt = 0
                for line in data.split('\n'):
                    cnt += 1
                    print(line)
                    input("Press Enter to continue") if cnt % 30 == 0 else None
            else:
                x = {
                    "count": cnt,
                    "results": res,
                }
                print(json.dumps(x, indent=3))


        except Exception:
            #traceback.print_exc()
            print("You have an error in your query syntax")
            print(sqlResult)
            print('\033[92m' +data)

    def do_db(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        nosqlResult=""
        try:
            data = ("**** polygon: query **** \n"
                    " ##  Below are the tables can be queried\n"
                    "        image,dataset,annotation,training_set,version\n"
                    " ##  Sql query :\n"
                    " ##      Example: \n"
                    "               1. select * from images\n"
                    "               2. select * from dataset limit 5\n"
                    "               3. select objectName from annotation\n"
                    " ##  No sql query : \n"
                    "        Example: \n"
                    "                 db.<table_name>.find({'<column_name>':'<value>'})\n"
                    "                 db.<table_name>.count({'<column_name>':'<value>'})")
            if '|' in arg:
                x = arg.split("|")
                args = x[0]
                outptDisplay = True
            else:
                args = arg
                outptDisplay = False
            pharse="db"+args
            nosqlResult = rest_connect.nosqlreslt(pharse)

            error1=nosqlResult["error"]
            cnt=nosqlResult["count"]
            res=nosqlResult["results"]
            if(error1 !=None):
                print(nosqlResult)
                print('\033[92m' +data)
            elif(outptDisplay == True):
                x = {
                    "count": cnt,
                    "results": res,
                }
                data = simplejson.dumps(x, indent=4)
                cnt = 0
                for line in data.split('\n'):
                    cnt += 1
                    print(line)
                    input("Press Enter to continue") if cnt % 30 == 0 else None
            else:
                x = {
                    "count": cnt,
                    "results": res,
                }
                print(json.dumps(x, indent=3))
        except:
            print("You have an error in your query syntax")
            print(nosqlResult)
            print('\033[92m' +data)


    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print(arg)
        print('Thank you for using Turtle1')
        self.close()
        bye()
        return True

    def do_clear(self, arg):
        print("\033c")

    def do_help(self, arg):
        data = ("**** polygon: query **** \n"                
                    " ##  Below are the tables can be queried\n"
                    "        image,dataset,annotation,training_set,version\n"
                    " ##  Sql query :\n"
                    " ##      Example: \n"
                    "               1. select * from images\n"
                    "               2. select * from dataset limit 5\n"
                    "               3. select objectName from annotation\n"
                    " ##  No sql query : \n"
                    "        Example: \n"
                    "                 db.<table_name>.find({'<column_name>':'<value>'})\n"
                    "                 db.<table_name>.count({'<column_name>':'<value>'})")
        print('\033[92m'+data)

    def pagetext(self,text_lined, num_lines=25):
        for index, line in enumerate(text_lined):
            if index % num_lines == 0 and index:
                input = raw_input("Hit any key to continue press q to quit")
                if input.lower() == 'q':
                    break
            else:
                print(line)

    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        # line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    PolygonShell().cmdloop()