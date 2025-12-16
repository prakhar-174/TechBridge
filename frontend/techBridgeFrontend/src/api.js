import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add a request interceptor to attach the token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

// Add a response interceptor to handle token expiration (optional but recommended)
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        // Handle 401 Unauthorized errors (e.g., redirect to login)
        if (error.response && error.response.status === 401) {
            localStorage.removeItem('accessToken');
            // window.location.href = '/auth'; // Optional: Force redirect
        }
        return Promise.reject(error);
    }
);

export default api;
