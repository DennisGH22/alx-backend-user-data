var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
var Teacher = /** @class */ (function () {
    function Teacher(firstName, lastName, options) {
        this.firstName = firstName;
        this.fullTimeEmployee = options.fullTimeEmployee;
        this.lastName = lastName;
        this.location = options.location;
        this.yearsOfExperience = options.yearsOfExperience;
        var fullTimeEmployee = options.fullTimeEmployee, yearsOfExperience = options.yearsOfExperience, location = options.location, additionalAttributes = __rest(options, ["fullTimeEmployee", "yearsOfExperience", "location"]);
        Object.assign(this, additionalAttributes);
    }
    return Teacher;
}());
var teacher3 = {
    firstName: 'John',
    fullTimeEmployee: false,
    lastName: 'Doe',
    location: 'London',
    contract: false,
};
console.log(teacher3);
