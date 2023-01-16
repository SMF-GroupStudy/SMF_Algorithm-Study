export default function Hello() {
    function showName(){
        console.log("Mike");
    }
    function showAge(age){
        console.log(age);
    }
    // function showText(e){
    //     console.log(e.target.value)
    //   이렇게 함수로 만들어서 {showText} 해도 되고
    //  밑에 처럼 해도댐.
    // }
     function showText(txt){
        console.log(txt);
    }
    return (
     <div>
        <h1>Hello</h1>
        <button onClick={showName}>Show name</button>
        <button onClick={() => {
            showAge(30)
        }}>
        Show age
        </button>
        <input type = "text" onChange={(e) =>{
            const txt = e.target.value;
            showText(txt);
            //console.log(e.target.value)
        }}></input>
     </div>
    );
}
// event
