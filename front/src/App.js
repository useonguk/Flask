import React, { useEffect, useState } from "react";
import styled from "styled-components";
import axios from "axios";

function App() {
  const [stores, setStores] = useState([]);
  const [shes, setShes] = useState([]);
  const [inventory, setInventory] = useState([]);

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

  const getShose = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/get_shose");
      console.log(response.data);
      setShes(response.data);
    } catch (error) {
      console.error(error);
    }
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
        {inventory.length === 0 && <div>신발이 없는 매장이와요</div>}
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
