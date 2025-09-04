### Girman Technologies

Custom Application

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch main
bench install-app girman_technologies
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/girman_technologies
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

### License

mit

## Features Implemented

- Part 1: Recruitment Workflow, Source field, Applicants by Source chart
- Part 2: Employee lifecycle automation and Experience Letter PDF
- Part 3: Salary Structure, Payroll Entry, Custom Payslip
- Part 4: Old/New Tax regime preference through Employee field + auto-structure
- Part 5: Investment Declaration Doctype and payroll linkage
