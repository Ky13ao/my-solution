// - **Bài 1:** Đếm số người của từng quốc gia.
// Kết quả trả về sẽ là:
// {
// 	"_id": "France",
// 	"total": 101238.0
// } {
// 	"_id": "Poland",
// 	"total": 98762.0
// }
db.people.aggregate({
	$group: {
		_id: "$address.country",
		total: {
			$sum: 1.0
		}
	}
});

// - **Bài 2:** Địa chỉ phổ biến nhất là gì và có bao nhiêu người sống ở đó?
// Kết quả trả về sẽ là:
// {
// 	"_id": {
// 		"country": "Poland",
// 		"city": "Warsaw",
// 		"postalCode": "02-495",
// 		"street": "Aleje Jerozolimskie"
// 	},
// 	"total": 5744.0
// }
db.people.aggregate([
	{
		$group: {
			_id: "$address",
			total: { $sum: 1 }
		}
	},
	{
		$sort: {
			total: -1
		}
	},
	{
		$limit: 1
	}
]);

// - **Bài 3:** Mỗi quốc gia có bao nhiêu người đã từng thanh toán ở một nhà hàng (restaurant)?
// Kết quả trả về sẽ là:
// {
// 	"_id": "France",
// 	"visits": 53126.0
// } {
// 	"_id": "Poland",
// 	"visits": 46971.0
// }

db.people.aggregate([
	{
		$match: {
			"payments.name": "restaurant"
		}
	},
	{
		$group: {
			_id: "$address.country",
			visits: {
				$sum: 1
			}
		}
	}
]);

// - **Bài 4:** Tìm 3 người có tổng số dư tài khoản nhiều nhất. Nếu như một người có cùng tổng số dư tài sản thì hãy so sánh bằng trường "firstName" và "lastName"
// Gợi ý: Các số dư tài sản được lưu trữ trong trường "wealth.bankAccounts.balance"
// Kết quả trả về sẽ là:
// {
// 	"firstName": "Mathilde",
// 	"lastName": "Bonnet",
// 	"totalBalance": 68544.28
// } {
// 	"firstName": "Maxime",
// 	"lastName": "Michel",
// 	"totalBalance": 67416.83
// } {
// 	"firstName": "Marie",
// 	"lastName": "Petit",
// 	"totalBalance": 66765.45
// }

db.people.aggregate([
	{
		$project: {
			_id: 0,
			firstName: 1,
			lastName: 1,
			totalBalance: {
				$round: [{ $sum: "$wealth.bankAccounts.balance" }, 2]
			}
		}
	},
	{
		$sort: { totalBalance: -1 }
	},
	{
		$limit: 3
	}
]);

// - **Bài 5:** Đếm số lần thanh toán ở nhà hàng, tổng số tiền đã chi tiêu và số tiền trung bình cho mỗi lần thanh toán chia theo từng quốc gia.
// Kết quả trả về sẽ là:
// {
// 	"_id": "France",
// 	"totalVisits": 78627.0,
// 	"totalAmount": 2958352.16000001,
// 	"avgAmount": 37.625143525761
// } {
// 	"_id": "Poland",
// 	"totalVisits": 66489.0,
// 	"totalAmount": 2026963.35,
// 	"avgAmount": 30.4856946261787
// }

db.people.aggregate([
	{ $unwind: "$payments" },
	{ $match: { "payments.name": "restaurant" } },
	{
		$group: {
			_id: "$address.country",
			totalVisits: {
				$sum: 1
			},
			totalAmount: {
				$sum: "$payments.amount"
			}
		}
	},
	{
		$project: {
			totalVisits: 1,
			totalAmount: 1,
			avgAmount: { $divide: ["$totalAmount", "$totalVisits"] }
		}
	},
	{
		$sort: {
			totalVisits: -1
		}
	}
]);

// - **Bài 6:** Có một quốc gia mà mức thanh toán trung bình tại một nhà hàng là cao nhất và một quốc gia trong đó mức thanh toán trung bình tại một nhà hàng thấp nhất. Số người của nước thứ nhất chi tiêu nhiều hơn người ở nước thứ hai bao nhiêu lần?
// Kết quả trả về sẽ là:
// {
// 	"_id": null,
// 	"diff": 1.23419013367179
// }

db.people.aggregate([
	{ $unwind: "$payments" },
	{ $match: { "payments.name": "restaurant" } },
	{
		$group: {
			_id: "$address.country",
			avgAmount: { $avg: "$payments.amount" }
		}
	},
	{
		$sort: {
			avgAmount: 1
		}
	},
	{
		$group: {
			_id: null,
			upperAvgAmount: { $last: "$avgAmount" },
			lowerAvgAmount: { $first: "$avgAmount" }
		}
	},
	{
		$project: {
			diff: { $divide: ["$upperAvgAmount", "$lowerAvgAmount"] }
		}
	}
]);

// - **Bài 7:**
// Viết truy vấn tìm tất cả những người có một hoặc nhiều giao dịch có giá trị bé hơn 5$. Kết quả trả về chỉ gồm các trường firstName, lastName và mảng payments  chứa TẤT CẢ phần tử có amount bé hơn 5$.
// Các Document trả về sẽ có cấu trúc như sau:
// {
// 	"_id": "5768667dbab6cf2f2fb5b63e",
// 	"firstName": "Igor",
// 	"lastName": "Kowalczyk",
// 	"payments": [
// 		{
// 			"category": "food",
// 			"name": "store",
// 			"amount": 4.54
// 		},
// 		{
// 			"category": "food",
// 			"name": "store",
// 			"amount": 4.56
// 		},
// 		{
// 			"category": "food",
// 			"name": "store",
// 			"amount": 3.05
// 		}
// 	]
// }
// Gợi ý: Bạn có thể lọc các phần tử thỏa mãn, sau đó dùng toán tử $push để gộp vào một mảng như yêu cầu đề bài.

db.people.aggregate([
	{ $unwind: "$payments" },
	{ $match: { "payments.amount": { $lt: 5 } } },
	{
		$group: {
			_id: {
				id: "$_id",
				firstName: "$firstName",
				lastName: "$lastName"
			},
			payments: { $push: "$payments" }
		}
	},
	{
		$project: {
			_id: "$_id.id",
			firstName: "$_id.firstName",
			lastName: "$_id.lastName",
			payments: 1
		}
	}
]);

// - **Bài 8:** Viết truy vấn để tính tổng giá trị mà một người đã thanh toán theo từng category.
// Các Document trả về sẽ có kết quả như sau:
// {
// 	"_id": {
// 		"$oid": "576865c0bab6cf2f2fb39d7a"
// 	},
// 	"firstName": "Lea",
// 	"lastName": "Bernard",
// 	"totalPayments": [{
// 			"category": "clothes",
// 			"amount": 315
// 		},
// 		{
// 			"category": "food",
// 			"amount": 5.57
// 		},
// 		{
// 			"category": "health",
// 			"amount": 28.22
// 		},
// 		{
// 			"category": "relax",
// 			"amount": 836.55
// 		}
// 	]
// },
// Gợi ý: Bạn có thể sử dụng toán tử $group kết hợp với $sum để tính tổng các khoản thanh toán theo category. Sau đó dùng $projection và $push để tạo mảng totalPayments theo như yêu cầu,

db.people.aggregate([
	{ $unwind: "$payments" },
	{
		$group: {
			_id: {
				id: "$_id",
				firstName: "$firstName",
				lastName: "$lastName",
				category: "$payments.category"
			},
			totalAmount: { $sum: "$payments.amount" }
		}
	},
	{
		$group: {
			_id: {
				id: "$_id.id",
				firstName: "$_id.firstName",
				lastName: "$_id.lastName"
			},
			totalPayments: {
				$push: {
					category: "$_id.category",
					amount: "$totalAmount"
				}
			}
		}
	},
	{
		$project: {
			_id: "$_id.id",
			firstName: "$_id.firstName",
			lastName: "$_id.lastName",
			totalPayments: 1
		}
	}
]);

// - **(Nâng cao) Bài 9:** Đếm số người ở mỗi quốc gia theo các nhóm tuổi như sau:
// 18-29
// 30-39
// 40-49
// Trước hết, số lượng người trong mỗi nhóm phụ thuộc vào ngày hiện tại. Nếu thực hiện truy vấn của mình hôm nay hoặc trong một tuần, chúng ta có thể nhận được các kết quả khác nhau. Điều này là do mọi người đang già đi mỗi ngày. Vì vậy, điều rất quan trọng là đặt một ngày tùy ý sẽ được sử dụng để tính tuổi của một người. Vậy nên chúng ta sẽ giả sử rằng ngày hiện tại là: 22/06/2016
// Kết quả trả về sẽ là:
// {
// 	"_id": {
// 		"country": "Poland",
// 		"ageRange": "18-29"
// 	},
// 	"count": 30742.0
// } {
// 	"_id": {
// 		"country": "France",
// 		"ageRange": "18-29"
// 	},
// 	"count": 31853.0
// } {
// 	"_id": {
// 		"country": "Poland",
// 		"ageRange": "40-49"
// 	},
// 	"count": 34800.0
// } {
// 	"_id": {
// 		"country": "France",
// 		"ageRange": "40-49"
// 	},
// 	"count": 35758.0
// } {
// 	"_id": {
// 		"country": "Poland",
// 		"ageRange": "30-39"
// 	},
// 	"count": 33220.0
// } {
// 	"_id": {
// 		"country": "France",
// 		"ageRange": "30-39"
// 	},
// 	"count": 33627.0
// }

db.people.aggregate([
	{
		$project: {
			_id: 1,
			country: "$address.country",
			age: {
				$dateDiff: {
					startDate: "$birthDate",
					endDate: { $toDate: "2016-06-22" },
					unit: "year"
				}
			}
		}
	},
	{
		$bucket: {
			groupBy: "$age",
			boundaries: [18, 30, 40, 50],
			default: "Others",
			output: {
				fromAge: { $min: "$age" },
				toAge: { $max: "$age" },
				countries: {
					$push: "$country"
				}
			}
		}
	},
	{
		$match: { _id: { $ne: "Others" } }
	},
	{
		$unwind: "$countries"
	},
	{
		$group: {
			_id: {
				country: "$countries",
				ageRange: {
					$concat: [{ $toString: "$fromAge" }, "-", { $toString: "$toAge" }]
				}
			},
			count: { $sum: 1 }
		}
	},
	{
		$sort: {
			count: 1
		}
	}
]);

// - **(Nâng cao) Bài 10:** Đếm số người ở mỗi quốc gia theo các nhóm tuổi như sau:
// Tính phần trăm dân số của cả nước thuộc các nhóm tuổi:
// 18-29
// 30-39
// 40-49
// Kết quả phải được làm tròn đến hai chữ số thập phân.
// Kết quả trả về sẽ là:
// {
// 	"_id": {
// 		"country": "Poland",
// 		"ageRange": "18-29"
// 	},
// 	"percent": 31.13
// } {
// 	"_id": {
// 		"country": "Poland",
// 		"ageRange": "40-49"
// 	},
// 	"percent": 35.24
// } {
// 	"_id": {
// 		"country": "Poland",
// 		"ageRange": "30-39"
// 	},
// 	"percent": 33.64
// } {
// 	"_id": {
// 		"country": "France",
// 		"ageRange": "18-29"
// 	},
// 	"percent": 31.46
// } {
// 	"_id": {
// 		"country": "France",
// 		"ageRange": "40-49"
// 	},
// 	"percent": 35.32
// } {
// 	"_id": {
// 		"country": "France",
// 		"ageRange": "30-39"
// 	},
// 	"percent": 33.22
// }

db.people.aggregate([
	{
		$project: {
			_id: 1,
			country: "$address.country",
			age: {
				$dateDiff: {
					startDate: "$birthDate",
					endDate: { $toDate: "2016-06-22" },
					unit: "year"
				}
			}
		}
	},
	{
		$bucket: {
			groupBy: "$age",
			boundaries: [18, 30, 40, 50],
			default: "Others",
			output: {
				fromAge: { $min: "$age" },
				toAge: { $max: "$age" },
				countries: {
					$push: "$country"
				}
			}
		}
	},
	{
		$match: { _id: { $ne: "Others" } }
	},
	{
		$unwind: "$countries"
	},
	{
		$group: {
			_id: "$countries",
			ageRanges: {
				$push: {
					$concat: [{ $toString: "$fromAge" }, "-", { $toString: "$toAge" }]
				}
			},
			population: { $sum: 1 }
		}
	},
	{
		$unwind: "$ageRanges"
	},
	{
		$group: {
			_id: {
				country: "$_id",
				ageRange: "$ageRanges"
			},
			count: { $sum: 1 },
			countryPopulation: { $first: "$population" }
		}
	},
	{
		$project: {
			_id: 1,
			percent: {
				$round: [
					{ $multiply: [{ $divide: ["$count", "$countryPopulation"] }, 100] },
					2
				]
			}
		}
	}
]);
