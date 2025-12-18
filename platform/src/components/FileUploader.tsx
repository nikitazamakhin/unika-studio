"use client";

import { useState, useRef } from "react";
import { fal } from "@fal-ai/client";

interface FileUploaderProps {
    label: string;
    onUpload: (url: string) => void;
    accept?: string;
    placeholder?: string;
}

export default function FileUploader({ label, onUpload, accept = "image/*", placeholder = "Upload file" }: FileUploaderProps) {
    const [uploading, setUploading] = useState(false);
    const [fileUrl, setFileUrl] = useState<string | null>(null);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) return;

        setUploading(true);
        try {
            const url = await fal.storage.upload(file);
            setFileUrl(url);
            onUpload(url);
        } catch (error) {
            console.error("Upload failed:", error);
            alert("Failed to upload file");
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="flex flex-col gap-2">
            <label className="text-sm text-gray-400 font-medium">{label}</label>
            <div
                className={`border border-dashed border-gray-700 bg-gray-900/50 rounded-lg p-4 text-center cursor-pointer hover:bg-gray-800 transition-colors ${uploading ? 'opacity-50 pointer-events-none' : ''}`}
                onClick={() => fileInputRef.current?.click()}
            >
                {fileUrl ? (
                    <div className="flex items-center justify-center gap-2">
                        <span className="text-green-500 text-sm">✅ Uploaded</span>
                        <img src={fileUrl} alt="Preview" className="w-8 h-8 rounded-full object-cover border border-gray-600" />
                    </div>
                ) : (
                    <div className="text-gray-500 text-sm">
                        {uploading ? "Uploading..." : placeholder}
                    </div>
                )}
                <input
                    type="file"
                    ref={fileInputRef}
                    className="hidden"
                    accept={accept}
                    onChange={handleFileChange}
                />
            </div>
        </div>
    );
}
