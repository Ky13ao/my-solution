use("asm2");

//education collection index
db.education.createIndex({ education_num: 1 }, { unique: true });

//occupation collection index
db.occupation.createIndex({
	occupation: 1,
	workclass: 1,
	income_bracket: 1,
	hours_per_week: 1
});
db.occupation.createIndex({ hours_per_week: 1 });
db.occupation.createIndex(
	{ workclass: 1 },
	{ partialFilterExpression: { workclass: "Private" } }
);

//relationship collection index
db.relationship.createIndex({ marital_status: 1, relationship: 1 });

//user collection index
db.user.createIndex({
	age: 1,
	gender: 1,
	race: 1,
	native_country: 1,
	"finance.total": 1,
	"finance.capital_gain": 1,
	"finance.capital_loss": 1
});
db.user.createIndexes([
	{ education_num: 1 },
	{ occupation_id: 1 },
	{ relationship_id: 1 },
	{ "finance.total": 1 }
]);
db.user.createIndex(
	{ native_country: 1 },
	{ partialFilterExpression: { native_country: "United-States" } }
);
