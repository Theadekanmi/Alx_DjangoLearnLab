import { PrismaClient } from '@prisma/client'
import bcrypt from 'bcryptjs'

const prisma = new PrismaClient()

async function main() {
  console.log('🌱 Starting database seeding...')

  // Create categories
  const categories = await Promise.all([
    prisma.category.upsert({
      where: { slug: 'ready-made' },
      update: {},
      create: {
        name: 'Ready-Made Clothing',
        slug: 'ready-made',
        description: 'Stylish ready-to-wear pieces for every occasion',
        image: 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400',
      },
    }),
    prisma.category.upsert({
      where: { slug: 'designs' },
      update: {},
      create: {
        name: 'Fashion Designs',
        slug: 'designs',
        description: 'Unique fashion designs and patterns',
        image: 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400',
      },
    }),
    prisma.category.upsert({
      where: { slug: 'fabrics' },
      update: {},
      create: {
        name: 'Premium Fabrics',
        slug: 'fabrics',
        description: 'High-quality fabrics for your creations',
        image: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
      },
    }),
  ])

  console.log('✅ Categories created')

  // Create products
  const products = await Promise.all([
    prisma.product.upsert({
      where: { slug: 'elegant-summer-dress' },
      update: {},
      create: {
        name: 'Elegant Summer Dress',
        slug: 'elegant-summer-dress',
        description: 'A beautiful summer dress perfect for any occasion. Made from premium cotton with a flattering fit.',
        price: 89.99,
        comparePrice: 129.99,
        sku: 'DSS-001',
        stock: 25,
        categoryId: categories[0].id,
        isFeatured: true,
        weight: 0.5,
        dimensions: { length: 80, width: 60, height: 5 },
      },
    }),
    prisma.product.upsert({
      where: { slug: 'classic-white-shirt' },
      update: {},
      create: {
        name: 'Classic White Shirt',
        slug: 'classic-white-shirt',
        description: 'Timeless white shirt for professional and casual wear. Made from 100% cotton.',
        price: 45.00,
        sku: 'CWS-001',
        stock: 50,
        categoryId: categories[0].id,
        weight: 0.3,
        dimensions: { length: 70, width: 50, height: 3 },
      },
    }),
    prisma.product.upsert({
      where: { slug: 'premium-cotton-fabric' },
      update: {},
      create: {
        name: 'Premium Cotton Fabric',
        slug: 'premium-cotton-fabric',
        description: 'High-quality cotton fabric for your sewing projects. 100% natural cotton, 200g/m².',
        price: 29.99,
        sku: 'PCF-001',
        stock: 100,
        categoryId: categories[2].id,
        weight: 0.2,
        dimensions: { length: 100, width: 150, height: 1 },
      },
    }),
    prisma.product.upsert({
      where: { slug: 'designer-pattern-set' },
      update: {},
      create: {
        name: 'Designer Pattern Set',
        slug: 'designer-pattern-set',
        description: 'Exclusive designer patterns for unique creations. Includes 5 different patterns.',
        price: 65.00,
        comparePrice: 85.00,
        sku: 'DPS-001',
        stock: 15,
        categoryId: categories[1].id,
        isFeatured: true,
        weight: 0.1,
        dimensions: { length: 30, width: 20, height: 2 },
      },
    }),
    prisma.product.upsert({
      where: { slug: 'silk-evening-gown' },
      update: {},
      create: {
        name: 'Silk Evening Gown',
        slug: 'silk-evening-gown',
        description: 'Luxurious silk evening gown for special occasions. Handcrafted with attention to detail.',
        price: 199.99,
        sku: 'SEG-001',
        stock: 8,
        categoryId: categories[0].id,
        isFeatured: true,
        weight: 0.8,
        dimensions: { length: 120, width: 80, height: 8 },
      },
    }),
    prisma.product.upsert({
      where: { slug: 'wool-blend-fabric' },
      update: {},
      create: {
        name: 'Wool Blend Fabric',
        slug: 'wool-blend-fabric',
        description: 'Warm and durable wool blend fabric. Perfect for winter garments.',
        price: 39.99,
        sku: 'WBF-001',
        stock: 75,
        categoryId: categories[2].id,
        weight: 0.4,
        dimensions: { length: 100, width: 150, height: 2 },
      },
    }),
  ])

  console.log('✅ Products created')

  // Create product images
  await Promise.all([
    prisma.productImage.upsert({
      where: { id: 'img-1' },
      update: {},
      create: {
        id: 'img-1',
        url: 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600',
        alt: 'Elegant Summer Dress',
        isPrimary: true,
        order: 0,
        productId: products[0].id,
      },
    }),
    prisma.productImage.upsert({
      where: { id: 'img-2' },
      update: {},
      create: {
        id: 'img-2',
        url: 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600',
        alt: 'Classic White Shirt',
        isPrimary: true,
        order: 0,
        productId: products[1].id,
      },
    }),
    prisma.productImage.upsert({
      where: { id: 'img-3' },
      update: {},
      create: {
        id: 'img-3',
        url: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600',
        alt: 'Premium Cotton Fabric',
        isPrimary: true,
        order: 0,
        productId: products[2].id,
      },
    }),
  ])

  console.log('✅ Product images created')

  // Create product variants
  await Promise.all([
    prisma.productVariant.upsert({
      where: { id: 'var-1' },
      update: {},
      create: {
        id: 'var-1',
        name: 'Size',
        value: 'Small',
        productId: products[0].id,
        stock: 10,
        sku: 'DSS-001-S',
      },
    }),
    prisma.productVariant.upsert({
      where: { id: 'var-2' },
      update: {},
      create: {
        id: 'var-2',
        name: 'Size',
        value: 'Medium',
        productId: products[0].id,
        stock: 15,
        sku: 'DSS-001-M',
      },
    }),
    prisma.productVariant.upsert({
      where: { id: 'var-3' },
      update: {},
      create: {
        id: 'var-3',
        name: 'Size',
        value: 'Large',
        productId: products[0].id,
        stock: 8,
        sku: 'DSS-001-L',
      },
    }),
  ])

  console.log('✅ Product variants created')

  // Create shipping zones
  const shippingZones = await Promise.all([
    prisma.shippingZone.upsert({
      where: { name: 'UK Domestic' },
      update: {},
      create: {
        name: 'UK Domestic',
        countries: ['GB'],
      },
    }),
    prisma.shippingZone.upsert({
      where: { name: 'EU' },
      update: {},
      create: {
        name: 'EU',
        countries: ['DE', 'FR', 'IT', 'ES', 'NL', 'BE', 'AT', 'IE'],
      },
    }),
  ])

  console.log('✅ Shipping zones created')

  // Create shipping methods
  await Promise.all([
    prisma.shippingMethod.upsert({
      where: { id: 'sm-1' },
      update: {},
      create: {
        id: 'sm-1',
        name: 'Standard Delivery',
        description: '3-5 business days',
        price: 3.99,
        freeThreshold: 50.00,
        minDays: 3,
        maxDays: 5,
        zoneId: shippingZones[0].id,
      },
    }),
    prisma.shippingMethod.upsert({
      where: { id: 'sm-2' },
      update: {},
      create: {
        id: 'sm-2',
        name: 'Express Delivery',
        description: '1-2 business days',
        price: 7.99,
        minDays: 1,
        maxDays: 2,
        zoneId: shippingZones[0].id,
      },
    }),
    prisma.shippingMethod.upsert({
      where: { id: 'sm-3' },
      update: {},
      create: {
        id: 'sm-3',
        name: 'International Standard',
        description: '5-10 business days',
        price: 12.99,
        minDays: 5,
        maxDays: 10,
        zoneId: shippingZones[1].id,
      },
    }),
  ])

  console.log('✅ Shipping methods created')

  // Create admin user
  const hashedPassword = await bcrypt.hash('admin123', 12)
  const adminUser = await prisma.user.upsert({
    where: { email: 'admin@fashionstore.com' },
    update: {},
    create: {
      email: 'admin@fashionstore.com',
      name: 'Admin User',
      password: hashedPassword,
      role: 'ADMIN',
    },
  })

  console.log('✅ Admin user created')

  // Create sample customer
  const customerPassword = await bcrypt.hash('customer123', 12)
  const customer = await prisma.user.upsert({
    where: { email: 'customer@example.com' },
    update: {},
    create: {
      email: 'customer@example.com',
      name: 'John Doe',
      password: customerPassword,
      role: 'CUSTOMER',
    },
  })

  console.log('✅ Sample customer created')

  // Create sample address
  await prisma.address.upsert({
    where: { id: 'addr-1' },
    update: {},
    create: {
      id: 'addr-1',
      type: 'SHIPPING',
      firstName: 'John',
      lastName: 'Doe',
      address1: '123 Main Street',
      city: 'London',
      state: 'England',
      postalCode: 'SW1A 1AA',
      country: 'GB',
      phone: '+44 20 7946 0958',
      isDefault: true,
      userId: customer.id,
    },
  })

  console.log('✅ Sample address created')

  console.log('🎉 Database seeding completed successfully!')
  console.log('\n📋 Sample Data:')
  console.log('- Admin user: admin@fashionstore.com / admin123')
  console.log('- Customer: customer@example.com / customer123')
  console.log('- Categories: Ready-Made Clothing, Fashion Designs, Premium Fabrics')
  console.log('- Products: 6 sample products with variants')
  console.log('- Shipping: UK and EU zones with multiple methods')
}

main()
  .catch((e) => {
    console.error('❌ Error seeding database:', e)
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })