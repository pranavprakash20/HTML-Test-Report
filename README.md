# HTML-Test-Report
To create html test execution reports

A sample usage can be found below

summary = OrderedDict() <br>
summary['Process 1'] = "Pass" <br>
summary['Process 2'] = "Pass" <br>
summary['Process 3'] = "Fail" <br>
summary['Process 4'] = "Fail" <br>
step_data = OrderedDict() <br>
step_data ["Step1"]="Some content here. Use <img> to add images" <br>
step_data ["Step2"]="Some content here. Use <img> to add images" <br>
step_data ["Step3"]="Some content here. Use <img> to add images" <br>
step_data ["Step3"]="Some content here. Use <img> to add images" <br>
obj = GenerateReport() <br>
obj.generate_report("Sample Heading", summary, step_data, "Sample Report") <br>
