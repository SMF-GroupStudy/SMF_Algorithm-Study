//fetch
import { useState } from 'react';
import { useEffect } from 'react';
import axios from 'axios';
//axios 라이브러리

const SERVER_URL = 'http://localhost:4000/api/todo';

//서버에 데이터를 요청할려면 서버 주소를 알아야하고, 어떤 http method를 사용할지 알아야됨.
//CORS 오류가 뜸. 
// 많이 만나는 오류임. 
//client : localhost 3001에 열려있는 개발서버가 열어주고 있음.
//server: localost:3000이 열어줌.
// origin(출저가 다름) 클라이언트는 포트 3001 서버는 3000 에서 옴
// origin이 다르니까 막 데이터를 꺼내가면 안됨. 오리진이 다르면 빼갈수 없는 정책에 막힘
// cors로 막아버린 정책은 누가 풀어줘야 하나? ---> 데이터를 줄지 말지를 정하는 서버에서 해결해야함.

// react-queary 를 통해 훅으로 만들면 좋음.
function App() {
  const [todoList, setTodoList] = useState(null);

  const fetchData = async () =>{
    // get응답이 왔으면 then 
    const response = await axios.get(SERVER_URL);
    setTodoList(response.data);
    // fetch('http://localhost:4000/api/todo')
    //   .then((response) => response.json())
    //   .then((data) => setTodoList(data));
  };

  useEffect(() => {
    fetchData();
  }, []);

  const onSubmitHandler = async (e) => {
    e.preventDefault();
    const text = e.target.text.value;
    const done = e.target.done.checked;
    await axios.post(SERVER_URL,{text, done});
    fetchData();
    // fetch('http://localhost:4000/api/todo', {
    //   method: 'POST',
    //   headers:{
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({
    //     text,
    //     done,
    //   }),
    // }).then(() => fetchData());

  }


  return (
    <div className="App">
      <h1>TODO LIST</h1>
      <form onSubmit={onSubmitHandler}>
        <input name="text" />
        <input name="done" type="checkbox" />
        <input type='submit' value="추가" />
      </form>
      {todoList?.map((todo) => (
        <div key={todo.id} style={{display:'flex'}}>
          <div>{todo.id}</div>
          <div>{todo.text}</div>
          <div>{todo.done ? 'Y' : 'N'}</div>
        </div>
      ))}
    </div>
  );
}

export default App;
