import React from "react";
import GetStoreInShos from "./getStoreInShos";
import PostShosePage from "./postshose";
import PostStorePage from "./postStore";

const LandingPage = ({ setState }) => {
  return (
    <>
      <div
        onClick={() => {
          setState("first");
        }}
      >
        렌딩 페이지
      </div>
      <div>
        <div>
          <GetStoreInShos />
        </div>
        <div>
          <PostShosePage />
        </div>
        <div>
          <PostStorePage />
        </div>
      </div>
    </>
  );
};

export default LandingPage;
