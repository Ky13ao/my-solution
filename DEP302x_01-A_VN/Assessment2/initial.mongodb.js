use("asm2");

function loadEducation() {
	const bulkInsert = db.education.initializeUnorderedBulkOp();
	//get all documents
	const documents = db.full.aggregate([
		{
			$group: {
				_id: {
					education: "$education",
					education_num: "$education_num"
				}
			}
		}
	]);

	//process each document
	documents.forEach(function ({ _id }) {
		const element = _id;
		bulkInsert.find(element).upsert().replaceOne(element);
	});

	bulkInsert.execute();
	return true;
}

function loadOccupation() {
	const bulkInsert = db.occupation.initializeUnorderedBulkOp();
	//get all documents
	const documents = db.full.aggregate([
		{
			$group: {
				_id: {
					occupation: "$occupation",
					workclass: "$workclass",
					hours_per_week: "$hours_per_week",
					income_bracket: "$income_bracket"
				}
			}
		}
	]);

	//process each document
	documents.forEach(function ({ _id }) {
		const element = _id;
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}

function loadRelationship() {
	const bulkInsert = db.relationship.initializeUnorderedBulkOp();
	//get all documents
	const documents = db.full.aggregate([
		{
			$group: {
				_id: {
					relationship: "$relationship",
					marital_status: "$marital_status"
				}
			}
		}
	]);

	//process each document
	documents.forEach(function ({ _id }) {
		const element = _id;
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}

function loadUser() {
	const bulkInsert = db.user.initializeUnorderedBulkOp();
	//get all documents
	const documents = db.full.find();

	//process each document
	documents.forEach(function (doc) {
		const element = {
			age: doc.age,
			race: doc.race,
			gender: doc.gender,
			native_country: doc.native_country,
			education_num: doc.education_num,
			finance: {
				total: doc.total,
				capital_gain: doc.capital_gain,
				capital_loss: doc.capital_loss
			}
		};
		const occupation = db.occupation.findOne({
			occupation: doc.occupation,
			workclass: doc.workclass,
			hours_per_week: doc.hours_per_week,
			income_bracket: doc.income_bracket
		});
		element.occupation_id = occupation._id;
		const relationship = db.relationship.findOne({
			relationship: doc.relationship,
			marital_status: doc.marital_status
		});
		element.relationship_id = relationship._id;
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}
