import React, { useState } from "react";
import axios from "axios";

const PostShosePage = () => {
  const [postShos, setPostShos] = useState({
    name: "",
    brand: "",
  });

  const AxiosPostShos = async (name, brand) => {
    try {
      console.log(name, brand);
      const response = await axios.post("http://127.0.0.1:5000/post_shoes", {
        name: name,
        brand: brand,
      });
      console.log(response.data);
    } catch (e) {
      console.error(e);
    }
  };
  return (
    <>
      <h1>신발 등록하기</h1>
      <input
        type="text"
        placeholder="신발 이름"
        value={postShos.name}
        onChange={(e) => setPostShos({ ...postShos, name: e.target.value })}
      />
      <input
        type="text"
        placeholder="회사명"
        value={postShos.brand}
        onChange={(e) => setPostShos({ ...postShos, brand: e.target.value })}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            AxiosPostShos(postShos.name, postShos.brand);
          }
        }}
      />
    </>
  );
};

export default PostShosePage;
