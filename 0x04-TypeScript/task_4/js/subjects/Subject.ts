import { Subjects as SubjectTeacher } from "./Teacher";

namespace Subjects {
    export class Subject {
        protected _teacher: SubjectTeacher.Teacher;

        setTeacher(teacher: SubjectTeacher.Teacher): void {
            this._teacher = teacher;
        }
    }
}

export { Subjects };
