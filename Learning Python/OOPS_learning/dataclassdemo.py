from dataclasses import dataclass
from typing import Any, Dict, List

# NEW CONCEPT: This comes from the pip repository. Make sure to do `pip install PyYAML` in your virtual env
import yaml


@dataclass
class Employee:
    firstName: str
    lastName: str
    salary: int


@dataclass()
class Company:
    company_name: str
    description: str
    employees: List[Employee]

    # NEW CONCEPT: Any validation or post processing can be done in post init.
    def __post_init__(self):
        employee_data = []
        for employee in self.employees:
            # NEW CONCEPT: The employee is an dictionary here, it is changed into Employee by doing **employee
            # *employee [ONE STAR] would mean assign values in the Employee one by one as defined by us.
            #       Eg. It does not matter if it has firstName, lastName. It will assign one by one.
            # **employee [TWO STARS] would assign values in the Employee BUT IT ALSO NEEDS TO MATCH THE PARAMETER NAME.
            #       Eg: firstName should be in the dictionary, lastName should be in here
            employee_data.append(Employee(**employee))
        self.employees = employee_data

    def get_monthly_salary(self) -> int:
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary


# step 1: Read the file. Since file is small, we are doing a whole read.
def read_yaml_file():
    with open("/home/paddy/python_workspace/appliedAiCourse/Learning Python/OOPS_learning/company.yaml") as company_yaml_file:
        return company_yaml_file.read()


# step 2: Parse the yaml file into a dictionary
def parse_yaml_file(yaml_string: str) -> Dict[Any, Any]:  # NEW CONCEPT: Any can be any type. Could be string, integer or anything
    return yaml.safe_load(yaml_string)


# step 3: Change dictionary into data class
def dict_to_company(parsed_yaml: Dict[Any, Any]) -> Company:
    print(parsed_yaml)
    return Company(**parsed_yaml)


# step 4: call the functions
read_yaml = read_yaml_file()
parsed_yaml_dict = parse_yaml_file(read_yaml)
mysteryInc = dict_to_company(parsed_yaml_dict)
# print("MysteryInc", mysteryInc, "Salary is ", mysteryInc.get_monthly_salary())