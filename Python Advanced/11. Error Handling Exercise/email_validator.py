from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class ContainMoreThenOneAtSymbolError(Exception):
    pass


domains = [".com", ".bg", ".org", ".net"]
domain_verification = r"\.[a-z]+"

email = input()

while email != "End":

    slice_email = email.split("@")

    if len(slice_email[0]) < 4:
        raise NameTooShortError("Name must be more than 4 characters!")

    if len(slice_email[-1]) < 6:
        raise InvalidDomainError("Please input valid email provider!")

    if email.count("@") <= 0:
        raise MustContainAtSymbolError("Email must contain @")

    if email.count("@") > 1:
        raise ContainMoreThenOneAtSymbolError("Email must contain only one @ symbol!")

    if findall(domain_verification, email)[-1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()