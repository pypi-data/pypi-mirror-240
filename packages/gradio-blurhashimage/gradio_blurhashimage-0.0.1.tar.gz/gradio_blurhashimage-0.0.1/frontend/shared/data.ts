import { normalise_file, FileData } from "@gradio/client";

export class BlurhashFileData {
	image?: FileData;
	blurhash?: string;
	width?: number;
	height?: number;
	constructor({ image, blurhash, width, height }: { image?: FileData; blurhash?: string; width?: number; height?: number }) {
		this.image = image ? new FileData(image) : undefined;
		this.blurhash = blurhash;
		this.width = width;
		this.height = height;
	}
}

export function normalise_blurhash_file(
	file: BlurhashFileData | null,
	server_url: string,
	proxy_url: string | null
): BlurhashFileData | null;

export function normalise_blurhash_file(
	file: BlurhashFileData[] | null,
	server_url: string,
	proxy_url: string | null
): BlurhashFileData[] | null;

export function normalise_blurhash_file(
	file: BlurhashFileData[] | BlurhashFileData | null,
	server_url: string, // root: string,
	proxy_url: string | null // root_url: string | null
): BlurhashFileData[] | BlurhashFileData | null;

export function normalise_blurhash_file(
	blurhash_file: BlurhashFileData[] | BlurhashFileData | null,
	server_url: string, // root: string,
	proxy_url: string | null // root_url: string | null
): BlurhashFileData[] | BlurhashFileData | null {
	if (blurhash_file == null) {
		return null;
	}

	if (Array.isArray(blurhash_file)) {
		const normalized_files: (BlurhashFileData | null)[] = [];

		for (const x of blurhash_file) {
			normalized_files.push(normalise_blurhash_file(x, server_url, proxy_url));
		}

		return normalized_files as BlurhashFileData[];
	}

	const file_data = blurhash_file.image ? normalise_file(blurhash_file.image, server_url, null) : null;

	return new BlurhashFileData({
		image: file_data ? file_data : undefined,
		blurhash: blurhash_file.blurhash,
		width: blurhash_file.width,
		height: blurhash_file.height,
	});
}