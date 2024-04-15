import React from "react";
import GetStoreInShos from "./getStoreInShos";
import PostShosePage from "./postshose";
import PostStorePage from "./postStore";

const LandingPage = () => {
  return (
    <>
      <div>렌딩 페이지</div>
      <div>
        <GetStoreInShos />
        <PostShosePage />
        <PostStorePage />
      </div>
    </>
  );
};

export default LandingPage;
