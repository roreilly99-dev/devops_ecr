/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    // Disable ESLint during build due to compatibility issues
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;
