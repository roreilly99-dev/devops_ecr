/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    // TODO: Fix ESLint compatibility issues with Next.js 15 and ESLint 9
    // Temporarily disabled during build. This should be resolved by:
    // 1. Waiting for eslint-config-next to support ESLint 9, or
    // 2. Downgrading to ESLint 8 with compatible config
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;
