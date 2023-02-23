import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "./css/index.css";
import { Provider, ErrorBoundary } from "@rollbar/react"; // Provider imports 'rollbar'

const el_main = document.getElementsByTagName("main")[0];
const root = ReactDOM.createRoot(el_main);

const rollbarConfig = {
  accessToken: process.env.ROLLBAR_ACCESS_TOKEN,
  environment: "gitpod-development",
};

function TestError() {
  const a = null;
  return a.hello();
}

root.render(
  <React.StrictMode>
    <Provider config={rollbarConfig}>
      <ErrorBoundary>
        {/* <TestError /> */}
        <App />
      </ErrorBoundary>
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
