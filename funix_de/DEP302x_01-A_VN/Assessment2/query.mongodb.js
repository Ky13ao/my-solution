use("asm2");

// Top 5 quốc gia có tổng số dư tài khoản lớn nhất
db.user.aggregate([
	{
		$group: {
			_id: "$native_country",
			total_balance: { $sum: "$finance.total" }
		}
	},
	{
		$sort: { total_balance: -1 }
	},
	{
		$limit: 5
	}
]);

// Tổng số người trong từng nhóm học vấn và nghề nghiệp
db.user.aggregate([
	{
		$lookup: {
			from: "education",
			localField: "education_num",
			foreignField: "education_num",
			as: "education"
		}
	},
	{
		$unwind: "$education"
	},
	{
		$lookup: {
			from: "occupation",
			localField: "occupation_id",
			foreignField: "_id",
			as: "occupation"
		}
	},
	{
		$unwind: "$occupation"
	},
	{
		$group: {
			_id: {
				education: "$education.education",
				occupation: "$occupation.occupation"
			},
			count: { $sum: 1 }
		}
	},
	{
		$sort: { count: -1 }
	}
]);

// Số lượng người làm việc nhiều hơn 40 giờ/tuần theo mức thu nhập
db.user.aggregate([
	{
		$lookup: {
			from: "occupation",
			localField: "occupation_id",
			foreignField: "_id",
			as: "occupation"
		}
	},
	{
		$unwind: "$occupation"
	},
	{
		$match: { "occupation.hours_per_week": { $gt: 40 } }
	},
	{
		$group: {
			_id: "$occupation.income_bracket",
			count: { $sum: 1 }
		}
	},
	{
		$project: {
			_id: 0,
			incomeBracket: "$_id",
			numberOfPeople: "$count"
		}
	}
]);

// Bình quân số tiền trong tài khoản và bình quân số giờ làm việc theo nghề nghiệp và mức giáo dục
db.user.aggregate([
	{
		$lookup: {
			from: "education",
			localField: "education_num",
			foreignField: "education_num",
			as: "education"
		}
	},
	{
		$unwind: "$education"
	},
	{
		$lookup: {
			from: "occupation",
			localField: "occupation_id",
			foreignField: "_id",
			as: "occupation"
		}
	},
	{
		$unwind: "$occupation"
	},
	{
		$group: {
			_id: {
				education: "$education.education",
				occupation: "$occupation.occupation"
			},
			avgAmount: { $avg: "$finance.total" },
			avgHoursPerWeek: { $avg: "$occupation.hours_per_week" }
		}
	},
	{
		$sort: { avgAmount: -1 }
	},
	{
		$project: {
			_id: 0,
			education: "$_id.education",
			occupation: "$_id.occupation",
			avgAmount: { $round: ["$avgAmount", 2] },
			avgHoursPerWeek: { $round: ["$avgHoursPerWeek", 2] }
		}
	}
]);

// Khoảng tuổi và và giờ làm việc mỗi tuần theo các khoảng phân loại theo tổng số dư trong tài khoản đối với các nghề nghiệp cá nhân
db.user.aggregate([
	{
		$lookup: {
			from: "occupation",
			localField: "occupation_id",
			foreignField: "_id",
			as: "occupation"
		}
	},
	{
		$match: { "occupation.workclass": "Private" }
	},
	{
		$unwind: "$occupation"
	},
	{
		$bucket: {
			groupBy: "$finance.total",
			boundaries: [10000, 20000, 50000, 100000, 200000, 500000],
			default: "others",
			output: {
				fromAmount: { $min: "$finance.total" },
				toAmount: { $max: "$finance.total" },
				sumOfAmount: { $sum: "$finance.total" },
				fromAge: { $min: "$age" },
				toAge: { $max: "$age" },
				sumOfAges: { $sum: "$age" },
				fromHPW: { $min: "$occupation.hours_per_week" },
				toHPW: { $max: "$occupation.hours_per_week" },
				sumOfHPW: { $sum: "$occupation.hours_per_week" },
				numberOfPeople: { $sum: 1 }
			}
		}
	},
	{
		$sort: { _id: 1 }
	},
	{
		$project: {
			_id: 0,
			amountRange: {
				$concat: [{ $toString: "$fromAmount" }, "-", { $toString: "$toAmount" }]
			},
			avgOfAmount: {
				$round: [{ $divide: ["$sumOfAmount", "$numberOfPeople"] }, 2]
			},
			ageRange: {
				$concat: [{ $toString: "$fromAge" }, "-", { $toString: "$toAge" }]
			},
			avgOfAges: {
				$round: [{ $divide: ["$sumOfAges", "$numberOfPeople"] }, 2]
			},
			hoursPerWeekRange: {
				$concat: [{ $toString: "$fromHPW" }, "-", { $toString: "$toHPW" }]
			},
			avgOfHourPerWeek: {
				$round: [{ $divide: ["$sumOfHPW", "$numberOfPeople"] }, 2]
			},
			numberOfPeople: 1
		}
	}
]);
