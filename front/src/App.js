import React, { useEffect, useState } from "react";
import PostShosePage from "./postshose";
import styled from "styled-components";
import axios from "axios";

function App() {
  const [postStore, setPostStore] = useState([]);
  const [stores, setStores] = useState([]);
  const [inventory, setInventory] = useState([]);
  const [shes, setShes] = useState([]);
  const [postShos, setPostShos] = useState({
    name: "",
    brand: "",
  });
  const [selectedShoe, setSelectedShoe] = useState({});
  const [quantity, setQuantity] = useState("");
  const [size, setSize] = useState(""); // 사이즈 상태 추가
  const [companies, setCompanies] = useState(); // 회사 목록 상태 추가

  useEffect(() => {
    getStore();
  }, []);

  const getStore = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/get_store");
      setStores(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const getStoreShose = async (storeId) => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/get_inventory/${storeId}`
      );
      console.log(response.data);
      setInventory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const AxiosPostStore = async (name, location) => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/post_store", {
        name: name,
        location: location,
      });
      console.log(response.data);
      setShes(response.data);
    } catch (e) {
      console.error(e);
    }
  };

  const getShose = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/get_shose");
      console.log(response.data);
      setShes(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const postInventory = async (shoe_name, brand, size, quantity) => {
    try {
      console.log(shoe_name);
      const response = await axios.post("http://127.0.0.1:5000/post_increase", {
        shoe_name: shoe_name,
        brand: brand,
        size: size,
        quantity: quantity,
      });
      console.log(response.data); // 성공 메시지 출력
      // 성공 메시지에 대한 추가적인 처리를 할 수 있습니다.
    } catch (error) {
      console.error(error); // 에러 처리
      // 에러에 대한 추가적인 처리를 할 수 있습니다.
    }
  };

  const handleAddInventory = () => {
    // postInventory 함수를 호출하여 데이터를 서버에 전송합니다.
    console.log(selectedShoe[0], companies);
    postInventory(selectedShoe[0], companies, size, quantity);
  };

  const handleShoeChange = (event) => {
    const selectedShoeIndex = event.target.value;
    const selectedShoeInfo = shes[selectedShoeIndex];
    console.log(selectedShoeInfo);
    setSelectedShoe(selectedShoeInfo);
  };

  const handleCompanyChange = (event) => {
    const selectedCompanyId = event.target.value;
    setCompanies(selectedCompanyId);
    // 선택된 회사의 ID를 사용하여 필요한 작업을 수행합니다.
    console.log("Selected Company ID:", selectedCompanyId);
  };

  return (
    <>
      <Sidebar>
        <SidebarContent>
          <RowCenter>
            <h2>Stores</h2>
            <h2
              onClick={() => {
                getShose();
              }}
            >
              Shos
            </h2>
          </RowCenter>
          <input
            type="text"
            placeholder="가게 이름"
            onChange={(e) => {
              setPostStore({ ...postStore, name: e.target.value });
            }}
          ></input>
          <input
            type="text"
            placeholder="가게 위치"
            onChange={(e) => {
              setPostStore({ ...postStore, location: e.target.value });
            }}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                AxiosPostStore(postStore.name, postStore.location);
              }
            }}
          ></input>
          <select onChange={handleCompanyChange}>
            <option value="">회사를 선택하세요</option>
            {stores.map((company, index) => (
              <option key={index} value={company[0]}>
                {company[1]}
              </option>
            ))}
          </select>
          <select onChange={handleShoeChange}>
            <option value="">신발을 선택하세요</option>
            {shes.map((shos, index) => (
              <option key={index} value={index}>
                {shos[1]}, {shos[2]}
              </option>
            ))}
          </select>
          <input
            type="number"
            placeholder="사이즈"
            value={size}
            onChange={(e) => setSize(e.target.value)}
          />

          <input
            type="number"
            placeholder="수량"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
          />
          <button onClick={handleAddInventory}>수량추가하기</button>
          <ul>
            {stores.map((store) => (
              <SidebarList
                key={store[0]}
                onClick={() => {
                  getStoreShose(store[0]);
                }}
              >
                {store[1]}, 위치: {store[2]}
              </SidebarList>
            ))}
          </ul>
          {Array.isArray(shes) && shes.length > 0 && (
            <ul>
              <h3>신발보기</h3>
              {shes.map((prev) => {
                return (
                  <SidebarList key={prev.id}>
                    {" "}
                    {/* 적절한 키를 사용하세요 */}
                    {prev.name}, {prev.brand}{" "}
                    {/* 필드명을 실제로 사용하는 필드명으로 변경하세요 */}
                  </SidebarList>
                );
              })}
            </ul>
          )}
        </SidebarContent>
      </Sidebar>
      <div style={{ margin: "30vw" }}>
        {inventory.map((prev, index) => {
          return (
            <div key={index}>
              {prev[0]}, {prev[1]}, {prev[2]}, {prev[3]},
            </div>
          );
        })}
      </div>
    </>
  );
}

export default App;

const Sidebar = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 30vw;
  background-color: yellow;
`;

const SidebarContent = styled.div`
  padding: 20px;
`;

const SidebarList = styled.li`
  cursor: pointer;
`;

const RowCenter = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
`;
