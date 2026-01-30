import "./globals.css";

export const metadata = {
  title: "Perth Events - Discover What's On",
  description: "Discover events in Perth including dining deals, outdoor cinema, markets, and sports",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
