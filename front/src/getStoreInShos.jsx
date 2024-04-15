const GetStoreInShos = () => {
  const [companies, setCompanies] = useState(); // 회사 목록 상태 추가
  const [selectedShoe, setSelectedShoe] = useState({});
  const [quantity, setQuantity] = useState("");
  const [size, setSize] = useState(""); // 사이즈 상태 추가

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

  const handleCompanyChange = (event) => {
    const selectedCompanyId = event.target.value;
    setCompanies(selectedCompanyId);
    // 선택된 회사의 ID를 사용하여 필요한 작업을 수행합니다.
    console.log("Selected Company ID:", selectedCompanyId);
  };

  const handleShoeChange = (event) => {
    const selectedShoeIndex = event.target.value;
    const selectedShoeInfo = shes[selectedShoeIndex];
    console.log(selectedShoeInfo);
    setSelectedShoe(selectedShoeInfo);

    const handleAddInventory = () => {
      // postInventory 함수를 호출하여 데이터를 서버에 전송합니다.
      console.log(selectedShoe[0], companies);
      postInventory(selectedShoe[0], companies, size, quantity);
    };
  };
  return (
    <>
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
