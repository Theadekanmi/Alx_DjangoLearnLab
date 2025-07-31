#!/bin/bash

echo "🚀 Setting up Fashion E-commerce Store..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Node.js and npm are installed"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Check if .env.local exists
if [ ! -f .env.local ]; then
    echo "📝 Creating .env.local file..."
    cp .env.example .env.local
    echo "⚠️  Please update .env.local with your configuration values"
    echo "   - DATABASE_URL: Your PostgreSQL connection string"
    echo "   - NEXTAUTH_SECRET: A random secret key"
    echo "   - STRIPE keys: Your Stripe API keys"
else
    echo "✅ .env.local already exists"
fi

# Generate Prisma client
echo "🔧 Generating Prisma client..."
npx prisma generate

echo ""
echo "🎉 Setup completed!"
echo ""
echo "📋 Next steps:"
echo "1. Update .env.local with your configuration"
echo "2. Set up your PostgreSQL database"
echo "3. Run: npm run db:migrate"
echo "4. Run: npm run db:seed (optional)"
echo "5. Run: npm run dev"
echo ""
echo "📚 For more information, see README.md"