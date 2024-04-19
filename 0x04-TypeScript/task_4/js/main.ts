import { Subjects } from "./subjects/Cpp";
import { Subjects as JavaSubjects } from "./subjects/Java";
import { Subjects as ReactSubjects } from "./subjects/React";

const cpp = new Subjects.Cpp();
const java = new JavaSubjects.Java();
const react = new ReactSubjects.React();

export const cTeacher = {
    firstName: "John",
    lastName: "Doe",
    experienceTeachingC: 10
};

console.log("C++:");
cpp.setTeacher(cTeacher);
console.log(cpp.getRequirements());
console.log(cpp.getAvailableTeacher());

console.log("Java:");
java.setTeacher(cTeacher);
console.log(java.getRequirements());
console.log(java.getAvailableTeacher());

console.log("React:");
react.setTeacher(cTeacher);
console.log(react.getRequirements());
console.log(react.getAvailableTeacher());
