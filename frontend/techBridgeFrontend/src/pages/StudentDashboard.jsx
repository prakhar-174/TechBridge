import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { FaRocket, FaChartPie, FaUserGraduate, FaArrowRight } from 'react-icons/fa';
import DashboardLayout from '../layouts/DashboardLayout';

const BenefitCard = ({ icon: Icon, title, description, delay }) => (
    <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay }}
        className="bg-white/5 border border-white/10 p-6 rounded-2xl hover:bg-white/10 transition-colors group"
    >
        <div className="w-12 h-12 rounded-xl bg-primary/20 flex items-center justify-center text-primary mb-4 group-hover:scale-110 transition-transform">
            <Icon className="text-xl" />
        </div>
        <h3 className="text-lg font-bold text-white mb-2">{title}</h3>
        <p className="text-gray-400 text-sm leading-relaxed">{description}</p>
    </motion.div>
);

const StudentDashboard = () => {
    return (
        <DashboardLayout>
            <div className="max-w-5xl mx-auto space-y-8">
                {/* Header */}
                <div>
                    <h1 className="text-3xl font-bold text-white mb-2">Welcome back, John! 👋</h1>
                    <p className="text-gray-400">Ready to take your skills to the next level?</p>
                </div>

                {/* Hero Assessment Card */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-primary to-purple-600 p-8 md:p-12"
                >
                    {/* Background Pattern */}
                    <div className="absolute inset-0 opacity-20">
                        <div className="absolute top-0 right-0 w-64 h-64 bg-white rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2" />
                        <div className="absolute bottom-0 left-0 w-64 h-64 bg-black rounded-full blur-[100px] translate-y-1/2 -translate-x-1/2" />
                    </div>

                    <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8">
                        <div className="max-w-xl">
                            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/20 backdrop-blur-sm border border-white/20 text-white text-xs font-medium mb-6">
                                <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
                                Recommended for you
                            </div>
                            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
                                Discover Your True Potential
                            </h2>
                            <p className="text-white/80 text-lg mb-8 leading-relaxed">
                                Take our comprehensive AI-driven assessment to identify your strengths and get a personalized learning roadmap tailored just for you.
                            </p>

                            <div className="flex flex-wrap items-center gap-6 mb-8">
                                <div className="flex items-center gap-2 text-white/90 text-sm">
                                    <FaChartPie /> 500+ Skills Assessed
                                </div>
                                <div className="w-1 h-1 rounded-full bg-white/40" />
                                <div className="flex items-center gap-2 text-white/90 text-sm">
                                    <FaRocket /> 15-20 min duration
                                </div>
                                <div className="w-1 h-1 rounded-full bg-white/40" />
                                <div className="flex items-center gap-2 text-white/90 text-sm">
                                    <FaUserGraduate /> Personalized Results
                                </div>
                            </div>

                            <Link
                                to="/assessment"
                                className="inline-flex items-center gap-2 px-8 py-4 bg-white text-primary font-bold rounded-xl hover:bg-gray-50 transition-all shadow-lg hover:shadow-xl hover:-translate-y-1"
                            >
                                Start Assessment <FaArrowRight />
                            </Link>
                        </div>

                        {/* Illustration Placeholder */}
                        <div className="hidden md:block relative w-64 h-64">
                            <div className="absolute inset-0 bg-white/10 backdrop-blur-md rounded-full animate-pulse" />
                            <div className="absolute inset-4 bg-white/20 backdrop-blur-md rounded-full" />
                            <div className="absolute inset-0 flex items-center justify-center">
                                <FaRocket className="text-6xl text-white drop-shadow-lg transform -rotate-45" />
                            </div>
                        </div>
                    </div>
                </motion.div>

                {/* Benefits Grid */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <BenefitCard
                        icon={FaChartPie}
                        title="Identify Skill Gaps"
                        description="Understand exactly where you stand in the current market and what you need to improve."
                        delay={0.2}
                    />
                    <BenefitCard
                        icon={FaRoute}
                        title="Personalized Roadmap"
                        description="Get a custom learning path designed specifically for your career goals and pace."
                        delay={0.3}
                    />
                    <BenefitCard
                        icon={FaUserGraduate}
                        title="Track Growth"
                        description="Monitor your progress over time with detailed analytics and milestone tracking."
                        delay={0.4}
                    />
                </div>

                {/* Recent Activity / Placeholder */}
                <div className="bg-white/5 border border-white/10 rounded-2xl p-6">
                    <h3 className="text-xl font-bold text-white mb-6">Recent Activity</h3>
                    <div className="text-center py-12 text-gray-400">
                        <div className="w-16 h-16 bg-white/5 rounded-full flex items-center justify-center mx-auto mb-4">
                            <FaClipboardList className="text-2xl opacity-50" />
                        </div>
                        <p>No assessments taken yet.</p>
                        <p className="text-sm mt-2">Complete your first assessment to see your history here.</p>
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
};

export default StudentDashboard;
