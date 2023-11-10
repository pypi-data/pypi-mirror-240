from raga import *
import datetime


run_name = f"ocr_test_analysis-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

test_session = TestSession(project_name="testingProject", run_name= run_name, access_key="75TS1h6fyP1SVBrtuOFd", secret_key="AIGc5XextI7s8RnWNbzPby9azQkmH374gcZ1eWvX", host="http://3.111.106.226:8080")


rules = OcrRules()
rules.add(expected_detection={"Merchant": 2,"Date": 1})



ocr_test = ocr_test_analysis(test_session=test_session,
                                            dataset_name = "Nano_Net_Dataset_3_nov_v11",
                                            test_name = "ocr_missing_value",
                                            model = "nanonet_model",
                                            type = "ocr",
                                            output_type="missing_value",
                                            rules = rules)

test_session.add(ocr_test)

test_session.run()