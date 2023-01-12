// 객체
const superman = {
    name:'clark',
    age:33,
}
//위 코드는 이렇게 줄일수도있음
// const name = 'clark' const age = 33;
const superman1 = {
    name,
    age,
    gender:'male',
}

console.log(superman.name);
console.log(superman['age']);
superman.hairColor = 'black'
superman['hobby'] = 'football';

delete superman.age;
console.log(superman);

// obejct 프로퍼티 존재 여부 확인 in을 사용
superman.birthDay; // undefined

function makeObject(name, age){
    return {
        name : name, // name,
        age : age, // age, 이렇게만 써도 댐
        hobby:"football"
    };
}

const Mike = makeObject("Mike", 30);
console.log(Mike);
console.log("age" in Mike);
console.log("birthday" in Mike)
console.log(Mike);

/*function isAdult2(user){
    if (user.age < 20){
        return false;
    }
        return true;
}*/

function isAdult2(user){
    if (!('age' in user) // user에 age가 없거나 
    || user.age < 20){ // 20살 미만 이거나
        return false;
    }
        return true;
}

const Jane = {
    name: 'Jane'
}
console.log(isAdult2(Jane)); // 나이를 입력하지 않았는데 true가 나옴.
console.log(isAdult2(Mike));

//for -- in 반복문
for(key in Mike){
    console.log(key)
    console.log(Mike[key])
    // key를 x라고 써도댐.
}

// method: 객체 프로퍼티로 할당 된 함수
let boy = {
    name:"Mike",
    showName: function () {
        console.log(this.name)
    }
};
console.log("----------------------------------------")
let man = boy;
man.name = "Tom"
console.log(boy.name);
man.showName;

boy = null;
//man. showName() -> 에러 뜸. 없어졌다고  근데 이럴땐 boy에 this를 쓰는거임.
// this는 () =>화살표 함수는 이용하지 않는게 좋음. 객체를 가르키는게 아니라 전역을 가르킴 windows
man.showName;

//배열
// push() 배열 끝에 요소 추가 pop는 제거 shift,unshift: 배열 앞에 제거/추가
// for of 문

let days = ['man', 'tue', 'wed'];
days[1] = '화요일'
console.log(days)
days.push("thu");
days.unshift("sun");

for(let index = 0; index < days.length; index++){
    console.log(days[index])
}

for (let day of days){
    console.log(day) // day는 요소 이기때문에 x라 써도 상관없음 아무 거나
}