import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});

export const fetchPosts = async () => {
  const response = await apiClient.get('/posts');
  return response.data;
};

export const fetchAnomalies = async () => {
  const response = await apiClient.get('/anomalies');
  return response.data;
};

export const fetchSummary = async () => {
  const response = await apiClient.get('/summary');
  return response.data;
};
