Lab7: Thực hành các thao tác CRUD

- Server: Mongo 7.0.2
- Tools:
  - Mongo Database Tools CLI version 100.9.0
  - Mongo Shell 2.0.2

```sh
mongoimport /uri:mongodb://localhost:27017/ /file:people.json /type:json /db:lab7 /collection:people /legacy /jsonArray
```

**Bài 1**: Đếm tất cả những người có tên là Pauline Fournier.

> Kết quả trả về sẽ là: 67.

```js
db.people.find({ firstName: "Pauline", lastName: "Fournier" }).count();
```

**Bài 2**: Đếm tất cả những người có tên là Pauline Fournier và sinh trước ngày 01/01/1970.

> Kết quả trả về sẽ là: 9.

```js
db.people
	.find({
		firstName: "Pauline",
		lastName: "Fournier",
		birthDate: { $lt: ISODate("1970-01-01") }
	})
	.count();
```

**Bài 3**: Đếm tất cả những người có tên:

Lucas Dubois
Camille Dubois

> Kết quả trả về sẽ là: 471.

```js
db.people
	.find({ firstName: { $in: ["Lucas", "Camille"] }, lastName: "Dubois" })
	.count();
```

**Bài 4**: Đếm tất cả những người không có khoản tín dụng (credits) nào. Bạn có thể tìm thấy các khoản tín dụng trong trường wealth.credits.,trường này là một mảng, vì mọi người có thể có một hoặc nhiều khoản tín dụng, nếu là mảng rỗng thì tức là không có khoản tín dụng nào.

> Kết quả trả về sẽ là: 83089.

```js
db.people.find({ "wealth.credits": { $size: 0, $type: "array" } }).count();
```

**Bài 5**: Đếm tất cả những người đã tiêu chính xác 12.99$ cho rạp chiếu phim (cinema). Tất cả các khoản thanh toán được lưu trữ trong trường mảng payments, bạn hãy xem qua cấu trúc các phần tử trong mảng này để viết truy vấn cho hợp lý.

> Kết quả trả về sẽ là: 270.

```js
db.people
	.find({ payments: { $elemMatch: { name: "cinema", amount: 12.99 } } })
	.count();
```

**Bài 6**: Hãy đếm tất cả những người có lần thanh toán đầu tiên là thanh toán 12.99$ cho rạp chiếu phim (cinema). Ở bài này bạn chỉ đếm các trường hợp có payments[0] thỏa mãn yêu cầu trên.

> Kết quả trả về sẽ là: 24.

```js
db.people
	.find({ "payments.0.name": "cinema", "payments.0.amount": 12.99 })
	.count();
```

**Bài 7**: Hãy đếm tất cả những người chưa bao giờ đến rạp chiếu phim (chưa có khoản thanh toán nào dành cho cinema).

> Kết quả trả về sẽ là: 79996.

```js
db.people.find({ "payments.name": { $ne: "cinema" } }).count();
```

**Bài 8**: Hãy đếm tất cả những phụ nữ đã chi hơn 100$ cho giày (shoes) và hơn 50$ cho quần (pants) trong 1 hóa đơn.

> Kết quả trả về sẽ là: 913.

```js
db.people
	.find({
		payments: {
			$all: [
				{ $elemMatch: { name: "shoes", amount: { $gt: 100 } } },
				{ $elemMatch: { name: "pants", amount: { $gt: 50 } } }
			]
		},
		sex: "female"
	})
	.count();
```

**Bài 9**: Hãy đếm tất cả những người từ Warsaw, Poland đã đến rạp chiếu phim (cinema) nhưng chưa bao giờ đến vũ trường (disco).

> Kết quả trả về sẽ là: 13352.

```js
db.people
	.find({
		$and: [
			{ "address.city": "Warsaw" },
			{ "address.country": "Poland" },
			{ "payments.name": "cinema" },
			{ "payments.name": { $ne: "disco" } }
		]
	})
	.count();
```

**Bài 10**: Đếm tất cả phụ nữ từ Paris và đàn ông từ Cracow mà có tất cả các tài sản sau:

- flat
- house
- land

Ít nhất một trong số các tài sản đó phải có giá trên 2.000.000$, và không tài sản nào trong số đó có giá dưới 500.000$.

Gợi ý, các tài sản được lưu trữ ở trường "wealth.realEstates"

> Kết quả trả về sẽ là: 23.

```js
db.people
	.find({
		$or: [
			{
				$and: [
					{ sex: "female" },
					{ "address.city": "Paris" },
					{ "wealth.realEstates.worth": { $not: { $lte: 500000 } } },
					{ "wealth.realEstates.worth": { $gt: 2000000 } },
					{ "wealth.realEstates.type": "house" },
					{ "wealth.realEstates.type": "land" },
					{ "wealth.realEstates.type": "flat" }
				]
			},
			{
				$and: [
					{ sex: "male" },
					{ "address.city": "Cracow" },
					{ "wealth.realEstates.worth": { $not: { $lte: 500000 } } },
					{ "wealth.realEstates.worth": { $gt: 2000000 } },
					{ "wealth.realEstates.type": "house" },
					{ "wealth.realEstates.type": "land" },
					{ "wealth.realEstates.type": "flat" }
				]
			}
		]
	})
	.count();
```

**Bài 11**: Đếm tất cả những người có đúng 10 giao dịch.

> Kết quả trả về sẽ là: 179972.

```js
db.people.find({ payments: { $size: 10 } }).count();
```

**Bài 12**: Tìm tất cả những người có `firstName` = 'Thomas' và chỉ trả về các trường sau: `_id`, `firstName` và `lastName`.

> Kết quả trả về sẽ có dạng như sau:
>
> ```json
> [
> 	{
> 		"_id": "576865c1bab6cf2f2fb39d7e",
> 		"firstName": "Thomas",
> 		"lastName": "Lambert"
> 	},
> 	{
> 		"_id": "576865c1bab6cf2f2fb39d9a",
> 		"firstName": "Thomas",
> 		"lastName": "Fournier"
> 	},
> 	...
> 	{
> 		"_id": "576865c2bab6cf2f2fb3a058",
> 		"firstName": "Thomas",
> 		"lastName": "Simon"
> 	}
> ]
> ```

```js
db.people.find({ firstName: "Thomas" }, { lastName: 1, firstName: 1 });
```

**Bài 13**: Tìm tất cả những người có một hoặc nhiều giao dịch có giá trị bé hơn 5$. Kết quả trả về chỉ gồm các trường firstName, lastName và payments chỉ chứa phần từ đầu tiên có amount bé hơn 5$.

> Ví dụ về kết quả trả về:
>
> ```json
> [
> 	{
> 		"_id": "576865c1bab6cf2f2fb39daa",
> 		"firstName": "Nicolas",
> 		"lastName": "Bernard",
> 		"payments": [{
> 			"category": "food",
> 			"name": "store",
> 			"amount": 3.47
> 		}]
> 	},
> 	{
> 		"_id": "576865c1bab6cf2f2fb39dbe",
> 		"firstName": "Kacper",
> 		"lastName": "Dabrowski",
> 		"payments": [{
> 			"category": "food",
> 			"name": "store",
> 			"amount": 3.16
> 		}]
> 	},
> 	...
> 	{
> 		"_id": "576865c1bab6cf2f2fb39fc6",
> 		"firstName": "Camille",
> 		"lastName": "Robert",
> 		"payments": [{
> 			"category": "food",
> 			"name": "store",
> 			"amount": 4.39
> 		}]
> 	}
> ]
> ```

```js
db.people.find(
	{ payments: { $elemMatch: { amount: { $lt: 5 } } } },
	{
		lastName: 1,
		firstName: 1,
		payments: { $elemMatch: { amount: { $lt: 5 } } }
	}
);
```

**Bài 14**: Thêm một phần tử vào payments của những người đang ở Pháp (France) với cấu trúc như sau:

```json
{
	"category": "relax",
	"name": "disco",
	"amount": 5.06
}
```

```js
db.yourCollection.updateMany(
	{ "address.country": "France" },
	{ $push: { payments: { category: "relax", name: "disco", amount: 5.06 } } }
);
```

**Bài 15**: Xóa tất cả các trường market của tất cả mọi người.

```js
db.people.updateMany({}, { $unset: { "wealth.market": 1 } });
```
