/*
변수 
예약어는 변수로 지정할 수 없음.
let const 
name 이라는 변수를 사용하면 나중에 다른 개발자가 와서 name = "google" 이렇게 사용하면 덮어버릴수 있음. 그럴 땐 let을 사용하면
다른 개발자가 쓸때 오류가남.
const 는 절대 바뀌지 않는 상수임 파이 생일 등을 입력할때 사용함.
변하지 않는 값은 const 변할수 있는 값은 let
1. 변수는 문자와 숫자 $,_만 사용
2. 첫글자는 숫자가 될 수 없다 ex) let 1stGrade = 'A+'; x
3. 예약어는 사용할 수 없다. ex) let let x
4. 가급적 상수는 대문자로 알려주는게 좋다. const MAX_SIZE = 99;
5. 변수명은 읽기 쉽고 이해할 수 있게 let a = 1; x let user_Num = 1; o

*/
let name5 = "Mike";
/*
문자형
*/
const name = "Mike"
const age = 30;

const name1 = "mike"  // 큰따옴표 가능
const name2 = 'Mike'  // 작은 따옴표
const name3 = `Mike`  // 왼쪽 상단 따옴표

const message = "I'm a boy." // 작은 따옴표를 넣을때 사용하면 좋음.
const message2 = 'I\'m a boy' // 특수문자로 인식할수도있음.
const message3 = `My name is ${name}`; // 베틱은 안에 변수를 $안에 넣으면 표기가능 ${age+10} 표현식도 가능

console.log(message3)

// Boolean 
//const a = true;
//const b = false;
// typeof 연산자 type이 반환됨.
console.log(typeof 3);
console.log(typeof true); 
// typeof null; -> object null은 근데 사실 object는 아님 (객체)

//alert은 알려주는 함수 알리는 용도 "비밀번호가 틀렸습니다. 이런거"
//prompt는 값을 입력받을때 사용

//const input = prompt("예약일을 입력해주세요.");
//alert("환영합니다" + input +"님" );
// prompt는 디폴트 값도 입력이 가능함. 웹일때 사용가능

// confirm()는 뭔가 확인을 받을때 사용함.
//const isAdult = confirm("당신은 성인 입니까?");
//console.log(isAdult) 취소를 누르면 false 확인은 True
//결제하시겟습니까? 이럴때 사용함.

//alert은 메시지를 보여줌 확인 
//prompt는 보여주고 답을 입력할 수 있음.
//confirm은 확인받는 용도 취소는 false 확인은 true
//창을 닫기전에는 스크립트 일시정지
// 스타일링 x

/*
형 변환
String() -> 문자형으로 변환
Number() -> 숫자형으로 변환
Boolean() -> 불린형으로 변환
prompt입력은 무조건 문자형임. "90" + "80" = 9080
근데 ("90" + "80" ) /2 = 4540 
"6" / "2" = 3 자동 형변환
명시적 형변환은
String(3) //"3"
Number("1234") // 1234 문자가있으면 NaN
Number(true) // 1 false 0
Boolean(0) //  0 , ""(빈문자열), null, undefined, NaN -> false 반환
//이외에는 true 반환
*/

/*
 2**3 은 2의 3승 거듭제곱임.
 증가 연산자 , 감소 연산자
 num ++; num --;
 앞이냐 뒤이냐 따라 다름.
 ++num 은 증가된 값을 넣는 것이고 num++은 증가되기 전값임
 result = ++num // 11
 result = num++ // 10
 */

/*
비교연산자
< > <= >= == !=
= 1개는 할당임 == 은 비교 연산
console.log(10>5) // true로 나옴 boolean 형으로 반환
*/ 
const a = 1;
const b = "1";

console.log(a == b);
// true임  값이 같아서 그데 ===면 타입까지 비교 일치 연산자임
console.log(a===b)


