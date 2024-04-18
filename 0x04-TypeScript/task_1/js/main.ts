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
