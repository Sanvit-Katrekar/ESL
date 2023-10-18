/** @type {import('next').NextConfig} */

// fixes npm run dev issue
const nextConfig = {
    webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
        config.externals.push({
          'utf-8-validate': 'commonjs utf-8-validate',
          'bufferutil': 'commonjs bufferutil',
        })
        return config
      },
}

module.exports = nextConfig