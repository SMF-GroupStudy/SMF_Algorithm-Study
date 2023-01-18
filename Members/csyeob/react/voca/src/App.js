import './App.css';
import DayList from './component/DayList';
import Header from './component/Header';
import Day from './component/Day'
import { BrowserRouter, Route, Routes } from "react-router-dom";
import EmptyPage from './component/EmptyPage';
import CreateWord from './component/CreateWord';
import CreateDay from './component/CreateDay';
function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<DayList />}></Route>
          <Route path="/day/:day" element={<Day/>}></Route>
          <Route path="create_word" element={<CreateWord/>}></Route>
          <Route path="create_day" element={<CreateDay/>}></Route>
          <Route path="*" element={<EmptyPage/>}></Route>
        </Routes>
        {/* Switch가 6버전 이상에서는 사라짐 그래서 Routes로 써야댐 */}
      </div>
    </BrowserRouter>
  );
}

export default App;
