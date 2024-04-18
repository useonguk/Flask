import React, { useState, useEffect } from "react";
import axios from "axios";

const GetStoreInShos = () => {
  const [stores, setStores] = useState([]);
  const [shes, setShes] = useState([]);
  const [companies, setCompanies] = useState("");
  const [selectedShoe, setSelectedShoe] = useState({});
  const [quantity, setQuantity] = useState("");
  const [size, setSize] = useState("");

  useEffect(() => {
    getStore();
    getShose();
  }, []);

  const getStore = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/get_store");
      console.log("렌딩 가끼엏애멀햐", response.data);
      setStores(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const getShose = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/get_shose");
      console.log("렌딩신발", response.data);
      setShes(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const postInventory = async (shoe_name, brand, size, quantity) => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/post_increase", {
        shoe_name: shoe_name,
        brand: brand,
        size: size,
        quantity: quantity,
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCompanyChange = (event) => {
    const selectedCompanyId = event.target.value;
    setCompanies(selectedCompanyId);
  };

  const handleShoeChange = (event) => {
    const selectedShoeIndex = event.target.value;
    const selectedShoeInfo = shes[selectedShoeIndex];
    setSelectedShoe(selectedShoeInfo);
  };

  const handleAddInventory = () => {
    postInventory(selectedShoe[0], companies, size, quantity);
  };

  return (
    <>
      <h1>가계 신발 등록하기</h1>
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
    </>
  );
};

export default GetStoreInShos;
