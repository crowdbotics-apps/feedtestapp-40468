import { api_v1_post_list } from "../../store/feedtestappAPI/posts.slice.js";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import React from "react";
import { Text, StyleSheet, View } from "react-native";

const PostsFeedScreen = params => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(api_v1_post_list({}));
  }, []);
  return <View style={styles.container}>
      <Text style={styles.headingTxt}>Posts listing Screen</Text>
    </View>;
};

const styles = StyleSheet.create({
  container: {
    margin: 20,
    flex: 1,
    justifyContent: "space-around"
  },
  headingTxt: {
    fontSize: 24,
    fontWeight: "bold",
    padding: 2,
    marginVertical: 12
  }
});
export default PostsFeedScreen;