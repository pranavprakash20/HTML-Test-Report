# HTML-Test-Report
To create html test execution reports

A sample usage can be found below

summary = OrderedDict()
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
obj.generate_report("Sample Heading", summary, step_data, "Sample Report")
