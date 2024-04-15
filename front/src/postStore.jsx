import axios from "axios";

const PostStorePage = () => {
  const [postStore, setPostStore] = useState([]);

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
  return (
    <>
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
    </>
  );
};

export default PostStorePage;
