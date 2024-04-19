import { RowID, RowElement } from "./interface";
const CRUD = require("./crud.js");

const obj = { firstName: "Guillaume", lastName: "Salva" };
CRUD.insertRow(obj);

const newRowID: RowID = 125;

const updatedRow: RowElement = { ...obj, age: 23 };
CRUD.updateRow(newRowID, updatedRow);

CRUD.deleteRow(newRowID);
