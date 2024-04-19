interface TeacherOptions {
    fullTimeEmployee: boolean;
    yearsOfExperience?: number;
    location: string;
    [key: string]: any;
}

class Teacher {
    readonly firstName: string;
    readonly lastName: string;
    fullTimeEmployee: boolean;
    yearsOfExperience?: number;
    location: string;
    [key: string]: any;

    constructor(firstName: string, lastName: string, options: TeacherOptions) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullTimeEmployee = options.fullTimeEmployee;
        this.yearsOfExperience = options.yearsOfExperience;
        this.location = options.location;

        const { fullTimeEmployee, yearsOfExperience, location, ...additionalAttributes } = options;
        Object.assign(this, additionalAttributes);
    }
}

const teacher3: Teacher = {
  firstName: 'John',
  fullTimeEmployee: false,
  lastName: 'Doe',
  location: 'London',
  contract: false,
};

console.log(teacher3);

interface Directors extends Teacher {
    numberOfReports: number;
}

class Director implements Directors {
    readonly firstName: string;
    readonly lastName: string;
    fullTimeEmployee: boolean;
    yearsOfExperience?: number;
    location: string;
    numberOfReports: number;
    [key: string]: any;

    constructor(firstName: string, lastName: string, options: TeacherOptions & { numberOfReports: number }) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullTimeEmployee = options.fullTimeEmployee;
        this.yearsOfExperience = options.yearsOfExperience;
        this.location = options.location;
        this.numberOfReports = options.numberOfReports;

        const { fullTimeEmployee, yearsOfExperience, location, numberOfReports, ...additionalAttributes } = options;
        Object.assign(this, additionalAttributes);
    }
}

const director1: Directors = {
	firstName: 'John',
	lastName: 'Doe',
	location: 'London',
	fullTimeEmployee: true,
	numberOfReports: 17,
};
console.log(director1);

interface PrintTeacherFunction {
    (firstName: string, lastName: string): string;
}

const printTeacher: PrintTeacherFunction = (firstName: string, lastName: string): string => {
    const firstInitial = firstName.charAt(0).toUpperCase();
    const fullLastName = lastName.charAt(0).toUpperCase() + lastName.slice(1);
    return `${firstInitial}. ${fullLastName}`;
};

console.log(printTeacher("John", "Doe"));

interface StudentClassConstructor {
    new(firstName: string, lastName: string): StudentClass;
}

interface StudentClass {
    workOnHomework(): string;
    displayName(): string;
}

class Student implements StudentClass {
    firstName: string;
    lastName: string;

    constructor(firstName: string, lastName: string) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    workOnHomework(): string {
        return "Currently working";
    }

    displayName(): string {
        return this.firstName;
    }
}

const studentInstance = new Student("John", "Doe");
console.log(studentInstance.workOnHomework());
console.log(studentInstance.displayName());
