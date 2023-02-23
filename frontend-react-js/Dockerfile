FROM node:19.6.1-bullseye-slim

ENV PORT=3000

COPY . /frontend-react-js

WORKDIR /frontend-react-js

RUN npm install

RUN apt-get update && apt-get install -y \
  curl \
  && rm -rf /var/lib/apt/lists/*

EXPOSE ${PORT}

CMD ["npm", "start"]