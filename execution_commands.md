##### Test execution based on 'marks/suites' (smoke, regression)
```sh
py.cleanup -p && py.test -m smoke --alluredir ExecutionResults/
py.cleanup -p && py.test -m regression --alluredir ExecutionResults/
```

##### Report Portal Commands
```sh
py.cleanup -p && py.test --reportportal
py.cleanup -p && py.test -m regression --reportportal
py.cleanup -p && py.test -m smoke --alluredir ExecutionResults/ --reportportal
```

##### Trigger Allure Reports
```sh
allure serve ExecutionResults
```
