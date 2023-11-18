from http_client.client import get_website
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch any homepage")
    parser.add_argument("server", help="Server or domain name")
    parser.add_argument("--port", type=int, default=80, help="Port number (default: 80)")
    parser.add_argument("--path", default="/", help="Path to the homepage (default: /)")

    args = parser.parse_args()
    get_website(args.server, args.port, args.path)
