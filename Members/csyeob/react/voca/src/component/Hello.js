import World from "./World";
import styles from "./Hello.module.css";
// const Hello = function (){
//     <p>Hello</p>;
// };

//const Hello = () =>{
//     <p>Hello</p>;
//};

// export default Hello;

export default function Hello() {
    return (
        //  태그는 return 해줘야함.
        // jsx 는 하나의 태그만 만들수 있음. 그래서 div로 묶어줘야함.
        // or <> </> 빈태그로 감아줘도댐.
        // 객체로 작성을 해야함. style = {} 이런식으로 안에 작성
        // border-right x borderRight 카멜케이스로 작성해야함.
        <div>
            <h1 style = {
                {
                    color: '#f00',
                    borderRight : '2px solid #000',
                    marginBottom : '30px',
                    opacity : 1,
                }
            }>Hello</h1>
            <World/>
            <div className={styles.box}>Hello</div>
        </div>
    );
}