"""
Script to generate HTML reports.
Developed By : Pranav Prakash <pranav.prakash@in.abb.com>
Python Version : 2.7
External Packages : NIL
"""

# This is a html report generation utility. This utility is still under modification

from collections import OrderedDict


class GenerateReport():
    def __init__(self):
        pass

    def __generate_html_header(self):
        html_header ="""<!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
            #myDIV {
                width: 100%;
                padding: 50px 0;
                text-align: center;
                background-color: lightblue;
                margin-top: 20px;
            }
            table {
                border-collapse: collapse;
                border-spacing: 0;
                width: 100%;
                border: 1px solid #ddd;
            }
            
            th, td {
                text-align: center;
                padding: 16px;
            }
            
            th:first-child, td:first-child {
                text-align: left;
            }
            
            tr:nth-child(even) {
                background-color: #f2f2f2
            }
            
            .fa-check {
                color: green;
            }
            
            .fa-remove {
                color: red;
            }
            .collapsible {
                background-color: #777;
                color: white;
                cursor: pointer;
                padding: 18px;
                width: 100%;
                border: none;
                text-align: left;
                outline: none;
                font-size: 15px;
            }
            .active, .collapsible:hover {
                background-color: #555;
            }
            
            .content {
                padding: 0 18px;
                display: none;
                overflow: hidden;
                background-color: #f1f1f1;
            }
            </style>
            </head>
            <body bgcolor="#d7dfe2">"""
        return html_header

    def __generate_html_body(self, heading):
        html_body = """<h1 align="center">%s</h1><p></p><h2>Overview</h2>""" % (heading)
        return html_body

    def __generate_summary(self, summary_data):
        html_summary = """
            <table>
            <tr>
            <th style="width:50%ds">Patch Name</th>
            <th>Result</th>
            </tr>"""
        for key in summary_data:
            if summary_data[key] == "Pass":
                check = "fa fa-check"
            else:
                check = "fa fa-remove"
            html_summary += """<tr><td>%s</td><td><i class="%s"></i></td></tr>""" % (key, check)

        html_summary += """</table><p> </p>"""
        return html_summary

    def __generate_steps(self, step_details):
        test_step_details = ''
        for key in step_details:
            test_step_details += """<button class="collapsible">%s</button>
            <div class="content">
              <p>%s</p>
            </div>
            <p></p>
            """ % (key,step_details[key])
        test_step_details += """<p></p>
            <p></p>
            <script>
            var coll = document.getElementsByClassName("collapsible");
            var i;
            for (i = 0; i < coll.length; i++) {
                coll[i].addEventListener("click", function() {
                    this.classList.toggle("active");
                    var content = this.nextElementSibling;
                    if (content.style.display === "block") {
                        content.style.display = "none";
                    } else {
                        content.style.display = "block";
                    }
                });
            }
            </script>
            
            </body>
            </html>
            """
        return test_step_details

    def generate_report(self, heading, summary, step_details, save_as):
        report_file = self.__generate_html_header() + self.__generate_html_body(heading) + \
                      self.__generate_summary(summary) + self.__generate_steps(step_details)
        report_file = report_file.replace('\n', ' ').replace('\r', '')
        html_result = open(save_as+"_Log.html", "w")
        html_result.write(report_file)
        html_result.close()

'''summary = OrderedDict()
summary['Process 1'] = "Pass"
summary['Process 2'] = "Pass"
summary['Process 3'] = "Fail"
summary['Process 4'] = "Fail"
step_data = OrderedDict()
step_data ["Step1"]="Some content here. Use <img> to add images"
step_data ["Step2"]="Some content here. Use <img> to add images"
step_data ["Step3"]="Some content here. Use <img> to add images"
step_data ["Step3"]="Some content here. Use <img> to add images"
obj = GenerateReport()
obj.generate_report("Sample Heading", summary, step_data, "Sample Report")'''