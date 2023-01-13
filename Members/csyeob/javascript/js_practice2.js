/*
    조건문 if else if else 
    사용방법은 똑같음.
    논리 연산자 ||(or) &&(and) !(not) 
*/
const gender = 'W';
const Name = 'Jane';
const isAdult = true;
//if(gender === 'M' && name === 'Mike' || isAdult) -> 통과가 나옴 왜냐 OR이 And보다 우선순위가 높음 그래서 isAdult만 true여도 true임
//if(gender === 'M' && (name === 'Mike' || isAdult)) -> 의도한 바대로 남자이고 마이크이거나 어른이면 true

/*
    반복문
    for(let i = 0; i < 10; i++){}
    let i = 0;
    while(i < 10){ i++ ;}
    do{
        i++;
    }while(i<10)
    while(true) --> 무한반복
    // do while은 일단 반복문 부터 수행한다는 점에서 한번은 실행함.
    break = 멈춤 continue 넘음.
*/
for( let i = 0; i< 10; i++){ // 0 2 4 6 8 짝수만
    if(i % 2){
        continue;
    }
    console.log(i);
}

// switch 문
/*
    switch(평가){
        case A:
            //a 코드 break;
        case B:
            // b 코드
            break;
        default : 
        ("그런 과일은 없습니다.");
    }
*/

// 함수(function)
// 매개변수는 ,로 구분해서 넣으면 됨.
function showError(){
    console.log('에러가 발생했스빈다. 다시시도해주세요.');
}

showError();
// default 값을 넣을 수 있음 매개변수에
function sayHello(name = 'friend'){
    let msg = `hello, ${name}`;
    console.log(msg);
}

sayHello();
sayHello("아ㅎ");

//return 값 반환 함수
function add(num1, num2){
    return num1 + num2;
}
console.log(add(2,3));

//함수 표현식
let sayHello2 = function(){
    console.log('Hello');
}

sayHello2();

// 함수선언문은 어디서든 호출 가능
// sayHello();
// function sayHello(){} ~ 있을때 sayhello를 먼저 호출했음에도 불구하고 실행이 됨. 이유는 어디서든 호출이 가능함.
// hoisiting으로 되기 때문에 가능한거임.
//함수 표현식은 코드에 도달하면 생성이 가능함.
// let sayHello = fucntion() ~ sayHello() 해야지 가능함.

/*
 화살표 함수
*/

let showError1 = function(){
    console.log('error');
};

let showError2 =(/*매개변수*/)=>{
    console.log('error');
};

showError1();
showError2();

const add2 = (num1, num2) => {
    const result = num1 + num2;
    return result;
};

console.log(add2(2,3));