// var 변수 한번 선언된 변수를 다시 선언할 수 있다. 호이스팅 
//var 은 1. 선언 및 초기화 단계 2. 할당 단계 선언및 초기화는 선언하면 undefined로 초기화됨.
//let 은 1. 선언단계 2. 초기화 단계 3. 할당 단계
//const 1. 선언 + 초기화 + 할당
var name = 'Mike' // Mike
var name = 'Jane' // jane
//함수 스코프  함수 안에 var를 만들면 당연히 전역변수로는 못씀
// var는 함수 스코프 안에서만 그럼
// var ㅂ다는 let 과 const로 사용하는것이 좋음.

// 객체 리터럴 생성자 함수 
// 함수명을 대문자로 하는게 암묵적인 약속 생성자함수는
function Item(title, price){
    this.title = title;
    this.price = price;
    this.showPrice = function(){
        console.log(`가격은 ${price} 원 입니다.`)
    }
}
const item1 = new Item('인형', 300);
const item2 = new Item('가방', 400);
// new를 뺀다면 그냥 Item 함수를 부르는 거임 그래서 undefined가 나옴.
console.log(item1, item2)
item1.showPrice();

let n = "name";
let a = "age";

const user = {
    [n]: "Mike",
    [a]: 30,
    [1+4]:[5],
};

console.log(user);

function makeObj(key, val){
    return {
        [key] : val
    };
}

const obj = makeObj("성별", "male")
// 어떤 키를 쓸지 모를땐 저렇게 씀.

const user1 = {
    name:"Mike",
    age : "30",
};
// const user2 = user 이것은 user 도 바뀜 
//그래서 복사를 할때는 Object.assign 메소드를 사용

const user2 = Object.assign({},user);
user2.name ="Tom";

console.log(user)
console.log(user2)

// Object.keys는 key값만 반환
const result = Object.keys(user);
console.log(result)
// value는 Object.values
//Object.entries 키값과 벨류값 둘다
// 0: ["키", "벨류"] 이런식

let arr = [
    ["mon","월"],
    ["tue", "화"],
];
// 배열을 객체로 만듬
const res = Object.fromEntries(arr);
console.log(res);

// 심볼형 Symbol 유일성 보장
const id = Symbol
// Symbol.for(): 전역심볼
// 하나의 심볼만 보장받을 수 있음. 없으면 만들고 있으면 가져오기 때문
// Symbol 함수는 매번 다른 Symbol 값을 생성하지만, Symbol.for 메소드는 하나를 생성한 뒤 키를 통해 같은 Symbol을 공유

// 다른 개발자가 만들어 놓은 객체
const o_dev = {
    name: "Mike",
    age: 30,
};

//내가 작업
// user.showName = function(){}; 이렇게 하지말고
const showName = Symbol("show name");
o_dev[showName] = function () {
    console.log(this.name);
};
o_dev[showName]();
//사용자가 접속하면 보는 메세지
for( let key in o_dev){
    console.log(`His ${key} is ${user[key]}.`)
}



