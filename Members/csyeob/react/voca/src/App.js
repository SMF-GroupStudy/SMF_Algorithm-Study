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
  return <div className="App">
    {/* <h1
      style={{
        color: "#f0f",
        backgroundColor:"green"
      }}>
      Hello, {name} <p>{2+3}</p>
    </h1> 
    <a href={naver.url}>{naver.name}</a> */}
    <Hello/>   
    <div className={styles.box}>App</div> 
  </div>;
}

export default App;
