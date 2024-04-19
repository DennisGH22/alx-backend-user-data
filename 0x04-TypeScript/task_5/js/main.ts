interface MajorCredits {
    credits: number;
    brand: "Major";
}

interface MinorCredits {
    credits: number;
    brand: "Minor";
}

function sumMajorCredits(subject1: MajorCredits, subject2: MajorCredits): MajorCredits {
    return {
        credits: subject1.credits + subject2.credits,
        brand: "Major"
    };
}

function sumMinorCredits(subject1: MinorCredits, subject2: MinorCredits): MinorCredits {
    return {
        credits: subject1.credits + subject2.credits,
        brand: "Minor"
    };
}

const subject1: MajorCredits = { credits: 3, brand: "Major" };
const subject2: MajorCredits = { credits: 4, brand: "Major" };
const majorSum = sumMajorCredits(subject1, subject2);
console.log("Sum of major credits:", majorSum);

const subject3: MinorCredits = { credits: 2, brand: "Minor" };
const subject4: MinorCredits = { credits: 1, brand: "Minor" };
const minorSum = sumMinorCredits(subject3, subject4);
console.log("Sum of minor credits:", minorSum);
