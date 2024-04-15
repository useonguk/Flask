import React, { useEffect, useState } from "react";
import styled from "styled-components";
import axios from "axios";
import LandingPage from "./landing";

function App() {
  const [page, setPage] = useState("first");
  const [stores, setStores] = useState([]);
  const [shes, setShes] = useState([]);
  const [inventory, setInventory] = useState([]);

  useEffect(() => {
    getStore();
    getShose();
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

  const groupedInventory = inventory.reduce((groups, item) => {
    const groupIndex = groups.findIndex((group) => group[0] === item[1]);
    if (groupIndex !== -1) {
      groups[groupIndex].push(item);
    } else {
      groups.push([item[1], item]);
    }
    return groups;
  }, []);

  return (
    <>
      {page === "first" ? (
        <>
          <Sidebar>
            <SidebarContent>
              <RowCenter>
                <h2>Stores</h2>
                <h2>Shos</h2>
                <h2
                  onClick={() => {
                    setPage("Landing");
                  }}
                >
                  등록하로 가기
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
                      <SidebarList key={prev[0]}>
                        {prev[1]}, {prev[2]}
                      </SidebarList>
                    );
                  })}
                </ul>
              )}
            </SidebarContent>
          </Sidebar>
          <div style={{ marginLeft: "35vw", marginTop: "30px" }}>
            {inventory.length === 0 && <div>신발이 없는 매장이와요</div>}
            {groupedInventory.map((group, index) => (
              <div key={index}>
                <h3>{group[0]}</h3>
                {group.slice(1).map((prev, idx) => (
                  <div key={idx}>
                    {prev[0]}, {prev[1]}, {prev[2]}, {prev[3]},
                  </div>
                ))}
              </div>
            ))}
          </div>
        </>
      ) : (
        <LandingPage setState={setPage} />
      )}
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
