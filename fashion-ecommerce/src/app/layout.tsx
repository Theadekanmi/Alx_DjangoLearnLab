import type { Metadata } from "next"
import { Inter } from "next/font/google"
import "./globals.css"
import { AuthProvider } from "@/components/providers/auth-provider"
import { Toaster } from "@/components/ui/toaster"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Fashion Store - Premium Fashion & Fabrics",
  description: "Discover our curated collection of fashion designs, ready-made clothing, and premium fabrics. Shop the latest trends with fast UK delivery.",
  keywords: "fashion, clothing, fabrics, UK, online store, ready-made, designer",
  authors: [{ name: "Fashion Store" }],
  openGraph: {
    title: "Fashion Store - Premium Fashion & Fabrics",
    description: "Discover our curated collection of fashion designs, ready-made clothing, and premium fabrics.",
    type: "website",
    locale: "en_GB",
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          {children}
          <Toaster />
        </AuthProvider>
      </body>
    </html>
  )
}
