import './App.css';
import Hello from './component/Hello';
import Welcome from './component/Welcome';
import styles from './App.module.css';
function App() {
  const name = "Tom"
  const naver = {
    name: "네이버",
    url: "https://naver.com",
  }
  return( 
  <div className="App">
    <Hello/>
    <Hello/>
    <Hello/>
    {/*useState는 컴포넌트 별로 관리를 함*/}
  </div>
  );
}

export default App;
